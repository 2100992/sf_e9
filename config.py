import os
from distutils.util import strtobool

# export DATABASE_URL= \
#     postgresql://postgres:docker@localhost:5432/weather_forecast_dev

DATABASE_URL = \
    'postgresql://postgres:docker@192.168.1.151:5432/weather_forecast_dev'


HOST = str(os.environ.get('HOST', 'localhost'))
PORT = int(os.environ.get('PORT', '5000'))


class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', DATABASE_URL)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SERVER_NAME = os.getenv('SERVER_NAME', f'{HOST}:{PORT}')
    DEBUG = strtobool(os.environ.get('DEBUG', 'True'))
    SECRET_KEY = os.getenv('SECRET_KEY', 'some_key_kjashf342jfhsd')

    if DEBUG:
        ENV = 'development'
        SESSION_COOKIE_DOMAIN = False
