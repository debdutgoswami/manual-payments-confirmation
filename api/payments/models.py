from payments import db

class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    public_id = db.Column(db.String(50), nullable=False)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return f"Admin('{self.name}', '{self.email}')"

class Participant(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    public_id = db.Column(db.String(50), nullable=False)
    name = db.Column(db.String(80), nullable=True)
    email = db.Column(db.String(50), nullable=False)
    department = db.Column(db.String(6), nullable=False)
    year = db.Column(db.String(5), nullable=False)
    student_chapter_id = db.Column(db.String(15), nullable=True)

    def __repr__(self):
        if self.student_chapter_id:
            return f"Participant('{self.name}', '{self.department}', '{self.student_chapter_id}')"
        else:
            return f"Participant('{self.name}', '{self.department}', '{None}')"
