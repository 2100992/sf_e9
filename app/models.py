from app import db


class Forecast(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, unique=False, nullable=False)
    city = db.Column(db.String(80), unique=False, nullable=False)
    temperature = db.Column(db.String(10), unique=False, nullable=False)
    precipitation = db.Column(db.Boolean, unique=False, nullable=True)


class User(db.Model):
    email = db.Column(db.String, primary_key=True)
    password = db.Column(db.String)
    authenticated = db.Column(db.Boolean, default=False)

    def get_id(self):
        return self.email

    def is_authenticated(self):
        return self.authenticated
