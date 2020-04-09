from app import app, db, bcrypt, login_manager

from flask import render_template, jsonify, make_response, request, redirect, url_for

from datetime import datetime

from app.models import Forecast, User
from app.extra import get_weather_for_date, Week
from app.forms import ForecastForm, LoginForm, CreateUserForm
from flask_login import login_user


@login_manager.user_loader
def user_loader(user_id):
    return User.query.get(user_id)


@app.errorhandler(404)
def page_not_found(e):
    title = "This page doesn't exist"
    return render_template('404.html', title=title), 404


@app.route('/')
def index():
    data = set('asdfgasdfg')
    return render_template('index.html', data=data)


@app.route('/hello')
def hello():
    return 'Hi, fellow Flask developer'


@app.route('/time')
def current_time():
    return make_response(jsonify(time=datetime.now()), 201)


@app.route('/week/<city>')
def weather_week(city):
    week = Week(datetime.today())
    week_weather = {day: get_weather_for_date(day) for day in week.week_days}
    return render_template(
        'week_overview.html',
        week=week,
        city=city,
        week_weather=week_weather
    )


@app.route('/forecast', methods=['POST', 'GET'])
def forecast():
    forecast_form = ForecastForm()
    if request.method == 'POST':
        print(forecast_form.validate())
        print(forecast_form.city.data)
        print(forecast_form.date.data)
        print(forecast_form.temperature.data)

        if forecast_form.validate_on_submit():

            city = forecast_form.city.data
            date = forecast_form.date.data
            temperature = forecast_form.temperature.data

            # date_format = datetime.strptime(date, '%Y-%m-%d')

            forecast = Forecast(
                city=city,
                # date=date_format.date(),
                date=date,
                # temperature=get_weather_for_date(date_format)
                temperature=temperature
            )

            db.session.add(forecast)
            db.session.commit()

            return redirect(url_for('index'))

        error = 'Form was not validated'
        return render_template('error.html', form=forecast_form, error=error)

    return render_template('add_forecast.html', form=forecast_form)


@app.route('/forecast/<_id>', methods=['GET', 'PATCH'])
def forecast_for_id(_id):
    if request.method == 'PATCH':
        temperature = request.args.get('temperature')

        forecast = Forecast.query.get_or_404(_id)
        forecast.temperature = temperature
        db.session.commit()

        return jsonify({'id': forecast._id}), 200

    elif request.method == 'GET':
        forecast = Forecast.query.get_or_404(_id)
        return jsonify({
            'id': forecast._id,
            'city': forecast.city,
            'temperature': forecast.temperature,
            'date': forecast.date
        })


@app.route('/forecast/<_id>', methods=['DELETE'])
def delete_forecast(_id):
    forecast = Forecast.query.get_or_404(_id)
    db.session.delete(forecast)
    db.commit()
    return jsonify({'result': True})


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.get(form.email.data)
        if user:
            if bcrypt.check_password_hash(user.password, form.password.data):
                user.authenticated = True
                # db.session.add(user)
                # db.session.commit()
                login_user(user, remember=True)
                return redirect(url_for('index'))
    return render_template('login.html', form=form)


@app.route("/create_user", methods=["GET", "POST"])
def create_user():
    form = CreateUserForm()
    if form.validate_on_submit():
        email = request.form.get('email')
        password = request.form.get('password')
        user = User(
            email=email, password=bcrypt.generate_password_hash(password))
        db.session.add(user)
        db.session.commit()
        return redirect("/")
    return render_template("login.html", form=form)
