from app import db
from datetime import datetime
from werkzeug.security import generate_password_hash,  check_password_hash
from flask_login import UserMixin


class Forecast(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, unique=False, nullable=False)
    city = db.Column(db.String(80), unique=False, nullable=False)
    temperature = db.Column(db.String(10), unique=False, nullable=False)
    precipitation = db.Column(db.Boolean, unique=False, nullable=True)


class Event(db.Model):
    __tablename__ = 'events'
    _id = db.Column(db.Integer, primary_key=True)
    author = db.relationship('User', backref='event', )
    start_time = db.Column(db.DateTime())
    end_time = db.Column(db.DateTime())
    title = db.Column(db.String(100), nullable=False)
    text = db.Column(db.Text(), nullable=True)

    def __init__(self):
        if self.start_time and self.end_time:
            if self.end_time < self.start_time:
                self.end_time = self.start_time


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    _id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(100), nullable=False)
    authenticated = db.Column(db.Boolean, default=False)
    username = db.Column(db.String(), nullable=False, default='Anonymous')
    updated_on = db.Column(
        db.DateTime(), default=datetime.utcnow, onupdate=datetime.utcnow)

    def __init__(self, email: str):
        self.email = email

    def get_id(self):
        return self.email

    def is_authenticated(self):
        return self.authenticated

    def __repr__(self):
        return f"<{self.email}>"

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self,  password):
        return check_password_hash(self.password_hash, password)

    def __str__(self):
        return self.__repr__()
