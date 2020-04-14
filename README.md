# Manual Payments Confirmation API

Portal APIs for manually confirming in-person payments. The main idea behind this is to have a list of due payments and one person behind the counter will mark the payment status as `Paid` once he/she pays the money and if a new person comes who has a payment due for future then a new `consumer` can be added with the default payment status as `Not Paid`. This can only be accessed by `Admin` (i.e. the staff)

---

## Libraries

1. Flask

2. Flask-SQLAlchemy

3. PyJWT

---

## How to setup for development

1. Clone this repository and change the directory to `manual-payments-confirmation`.

2. Create one file inside the `api` folder as `.flaskenv`. This will contain `FLASK CLI` parameters. Add the bellow lines into the file

    ```
    FLASK_APP=payments
    FLASK_ENV=development
    FLASK_RUN_HOST=0.0.0.0
    FLASK_RUN_PORT=8080
    ```

3. Create another file inside the `api/payments` folder as `.env`. This will contain the `FLASK CONFIG` values. Add the bellow lines into the file and make the necessary changes and addition.

    ```
    SECRET_KEY=yoursecretkey
    API_KEY=yourapikey
    SQLALCHEMY_DATABASE_URI=sqlite:///yourdatabasename.db
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    ```

4. Now open up the python interactive shell by typing `python3` in the terminal and enter the below code

    ```
    >>>from payments import db
    >>>db.create_all()
    ```

    This will create all the tables from the ORMs in `models.py` file into the database.

5. Now you are all setup. Just type `flask run` in your terminal to start the development server.

---