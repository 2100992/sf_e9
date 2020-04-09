from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
db.create_all()

login_manager = LoginManager()
login_manager.init_app(app)

bcrypt = Bcrypt(app)

from app import routes, models, forms
