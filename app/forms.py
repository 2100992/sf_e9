from flask_wtf import FlaskForm

from wtforms import StringField, PasswordField
from wtforms import SubmitField, TextAreaField

from wtforms.fields.html5 import EmailField

from wtforms.validators import DataRequired, Email
from wtforms.validators import InputRequired, EqualTo


class EventForm(FlaskForm):
    title = StringField(
        'Название',
        validators=[
            InputRequired(),
            DataRequired()
        ]
    )
    text = TextAreaField(
        'Описание события'
    )

    start_time = StringField(
        'Время начала события в формате',
        validators=[
            # InputRequired(),
            # DataRequired()
        ]
    )
    end_time = StringField(
        'Время окончания события в формате',
        validators=[
            # InputRequired(),
            # DataRequired()
        ]
    )
    submit = SubmitField('Добавить')


class LoginForm(FlaskForm):
    email = EmailField(
        'Укажите email',
        validators=[
            InputRequired("Please enter email."),
            DataRequired(),
            Email()
        ]
    )
    password = PasswordField(
        'Введите пароль',
        validators=[
            InputRequired("Please enter password."),
            DataRequired()
        ]
    )
    submit = SubmitField('Войти')


class CreateUserForm(FlaskForm):
    email = EmailField(
        'Введите email',
        validators=[
            InputRequired("Please enter email."),
            DataRequired(),
            Email()
        ]
    )
    password = PasswordField(
        'Введите пароль',
        validators=[
            InputRequired("Please enter password."),
            DataRequired()
        ]
    )
    password_conf = PasswordField(
        'Повторите пароль',
        validators=[
            InputRequired("Please confirm password."),
            DataRequired(),
            EqualTo('password', message='Different passwords')
        ]
    )
    submit = SubmitField('Создать')


class EditUserForm(FlaskForm):
    username = StringField(
        'Имя пользователя',
        validators=[
            InputRequired(),
            DataRequired()
        ]
    )
    email = EmailField(
        'Укажите email',
        validators=[
            DataRequired(),
            Email()
        ]
    )

    submit = SubmitField('Внести изменения')
