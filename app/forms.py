from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.fields.html5 import DateField, EmailField
from wtforms.validators import DataRequired, Email, InputRequired


class ForecastForm(FlaskForm):
    city = StringField(
        'city',
        validators=[
            InputRequired("Please enter your city."),
            DataRequired()
        ]
    )
    date = DateField(
        'date',
        format='%Y-%m-%d',
        validators=[
            InputRequired("Please enter date."),
            DataRequired()
        ]
    )
    temperature = StringField(
        'temperature',
        validators=[
            InputRequired("Please enter temperature."),
            DataRequired()
        ]
    )
    submit = SubmitField('Добавить')


class LoginForm(FlaskForm):
    email = EmailField('email', validators=[DataRequired(), Email()])
    password = PasswordField('password', validators=[DataRequired()])
    submit = SubmitField('Войти')

class CreateUserForm(FlaskForm):
    email = EmailField('Введите email', validators=[DataRequired(), Email()])
    password = PasswordField('Введите пароль', validators=[DataRequired()])
    password_conf = PasswordField('Повторите пароль', validators=[DataRequired()])
    submit = SubmitField('Создать')