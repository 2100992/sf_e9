from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, BooleanField
from wtforms.fields.html5 import EmailField, DateTimeField
from wtforms.validators import DataRequired, Email, InputRequired, EqualTo


class CreateEventForm(FlaskForm):
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

    start_time = DateTimeField(
        'Время начала события',
        format='%Y-%m-%d %H:%M:%S',
        validators=[
            InputRequired(),
            DataRequired()
        ]
    )
    end_time = DateTimeField(
        'Время окончания события',
        format='%Y-%m-%d %H:%M:%S',
        validators=[
            InputRequired(),
            DataRequired()
        ]
    )


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


class ChangeUserForm(FlaskForm):
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
    # password = PasswordField(
    #     'Введите пароль',
    #     validators=[
    #         DataRequired()
    #     ]
    # )
    # password_conf = PasswordField(
    #     'Повторите пароль',
    #     validators=[
    #         DataRequired(),
    #         EqualTo('password', message='Different passwords')
    #     ]
    # )
    # authenticated = BooleanField(
    #     'Авторизованный пользователь',
    #     validators=[
    #         # DataRequired()
    #     ]
    # )

    submit = SubmitField('Внести изменения')
