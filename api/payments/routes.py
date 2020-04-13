from flask import request,  jsonify, make_response
from payments.models import Admin, Participant
from payments import app, db
import uuid
from werkzeug.security import generate_password_hash, check_password_hash
# import PyJWT authentication
from functools import wraps
import jwt, datetime

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']

        if not token:
            return jsonify({'message' : 'Token is missing!!'}), 401

        try:
            data = jwt.decode(token, app.config['SECRET_KEY'])
            current_user = Admin.query.filter_by(public_id=data['public_id']).first()
        except:
            return jsonify({'message' : 'Token is invalid!!'}), 401

        return f(current_user, *args, **kwargs)

    return decorated

@app.route('/participants', methods=['GET', 'POST'])
@token_required
def participants(current_user):
    if request.method == 'GET':
        participants = Participant.query.all()

        output = []
        for participant in participants:
            output.append({
                'name' : participant.name,
                'email' : participant.email,
                'department' : participant.department,
                'year' : participant.year,
                'student_chapter_id' : participant.student_chapter_id
            })

        return jsonify({'participants' : output})

    elif request.method == 'POST':
        participant = request.get_json()

        new_participant = Participant(public_id=str(uuid.uuid4()), name=participant['name'], email=participant['email'], department=participant['department'],
                                        year=participant['year'], student_chapter_id=participant['student_chapter_id'], payment_status=False)

        db.session.add(new_participant)
        db.session.commit()

        return jsonify({'message' : 'Successfully added participant!'})

@app.route('/admin', methods=['POST'])
def create_admin():
    data = request.get_json()

    hashed_password = generate_password_hash(data['password'], method='sha256')

    new_admin = Admin(public_id=str(uuid.uuid4()), name=data['name'], email=data['email'], password=hashed_password)

    db.session.add(new_admin)
    db.session.commit()

@app.route('/login', method=['POST'])
def login():
    auth = request.get_json()

    if not auth or not auth['email'] or not auth['password']:
        return make_response('Could not verify!!', 401)

    admin = Admin.query.filter_by(email=auth['email']).first()

    if not admin:
        return make_response('Could not verify!!', 401)

    if check_password_hash(admin.password, auth['password']):
        token = jwt.encode({'public_id' : admin.public_id, 'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=120)}, app.config['SECRET_KEY'])

        return jsonify({'token' : token.decode('UTF-8')})

    return make_response('Could not verify!!', 401)
