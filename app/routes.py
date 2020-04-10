from app import app, db
# from app import bcrypt
from app import login_manager

from flask import request
from flask import render_template
# from flask import jsonify
# from flask import make_response
from flask import redirect, url_for
from flask import flash

from datetime import datetime

from app.models import User, Event
# from app.extra import get_weather_for_date, Week
from app.forms import LoginForm, CreateUserForm
from app.forms import CreateEventForm, ChangeUserForm
from flask_login import login_user, login_required, logout_user, current_user


@login_manager.user_loader
def user_loader(user_id):
    return User.query.get(user_id)


@app.errorhandler(404)
def page_not_found(e):
    title = "This page doesn't exist"
    return render_template('404.html', title=title), 404


@app.route('/')
# @login_required
def index():
    data = {}
    data['text'] = 'new text'
    # data['user'] = request.user.email
    return render_template('index.html', data=data)


@app.route('/hello')
def hello():
    return 'Hi, fellow Flask developer'



# @app.route('/week/<city>')
# def weather_week(city):
#     week = Week(datetime.today())
#     week_weather = {day: get_weather_for_date(day) for day in week.week_days}
#     return render_template(
#         'week_overview.html',
#         week=week,
#         city=city,
#         week_weather=week_weather
#     )


# @app.route('/forecast', methods=['POST', 'GET'])
# def forecast():
#     forecast_form = ForecastForm()
#     if request.method == 'POST':

#         if forecast_form.validate_on_submit():

#             city = forecast_form.city.data
#             date = forecast_form.date.data
#             temperature = forecast_form.temperature.data

#             # date_format = datetime.strptime(date, '%Y-%m-%d')

#             forecast = Forecast(
#                 city=city,
#                 # date=date_format.date(),
#                 date=date,
#                 # temperature=get_weather_for_date(date_format)
#                 temperature=temperature
#             )

#             db.session.add(forecast)
#             db.session.commit()

#             return redirect(url_for('index'))

#         error = 'Form was not validated!!!'
#         return render_template('error.html', form=forecast_form, error=error)

#     return render_template('add_forecast.html', form=forecast_form)


# @app.route('/forecast/<_id>', methods=['GET', 'PATCH'])
# def forecast_for_id(_id):
#     if request.method == 'PATCH':
#         temperature = request.args.get('temperature')

#         forecast = Forecast.query.get_or_404(_id)
#         forecast.temperature = temperature
#         db.session.commit()

#         return jsonify({'id': forecast._id}), 200

#     elif request.method == 'GET':
#         forecast = Forecast.query.get_or_404(_id)
#         return jsonify({
#             'id': forecast._id,
#             'city': forecast.city,
#             'temperature': forecast.temperature,
#             'date': forecast.date
#         })


# @app.route('/forecast/<_id>', methods=['DELETE'])
# def delete_forecast(_id):
#     forecast = Forecast.query.get_or_404(_id)
#     db.session.delete(forecast)
#     db.commit()
#     return jsonify({'result': True})


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            user = User.query.filter_by(email=form.email.data).first()
            print(user)
            if user.check_password(form.password.data):
                # user.authenticated = True
                # db.session.add(user)
                # db.session.commit()
                login_user(user, remember=True)
                return redirect(url_for('index'))
    title = 'Войти'
    return render_template('login.html', form=form, title=title)


@app.route("/create_user", methods=["GET", "POST"])
def create_user():
    form = CreateUserForm()
    if form.validate_on_submit():
        flash('create_user form.validate_on_submit()')
        email = form.email.data
        password = form.password.data
        user = User(email)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        return redirect("/")
    title = 'Создать пользователя'
    return render_template("login.html", form=form, title=title)


@app.route('/user', methods=['GET', 'POST'])
# @login_required
def user():
    form = ChangeUserForm()
    if request.method == 'POST':
        print('POST')
        if form.validate_on_submit():
            user = User.query.filter_by(_id=current_user._id).first()
            if form.email.data:
                user.email = form.email.data
            if form.username.data:
                user.username = form.username.data
            # if form.password.data:
            #     user.set_password(form.password.data)
            db.session.commit()
            login_user(user, remember=True)
        return redirect(url_for('user'))

    if current_user.is_authenticated:
        form.email.data = current_user.email
        form.username.data = current_user.username
        return render_template('user.html', form=form)
    return redirect(url_for('login'))

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash("You have been logged out.")
    return redirect(url_for('login'))
