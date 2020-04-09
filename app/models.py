from app import db
from datetime import datetime
from werkzeug.security import generate_password_hash,  check_password_hash


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
    updated_on = db.Column(
        db.DateTime(), default=datetime.utcnow, onupdate=datetime.utcnow)

    def get_id(self):
        return self.email

    def is_authenticated(self):
        return self.authenticated

    def __repr__(self):
        return f"<{self._id}:{self.email}>"

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self,  password):
        return check_password_hash(self.password_hash, password)
