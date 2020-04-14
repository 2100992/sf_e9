from app import app, db

from app import login_manager

from flask import request
from flask import render_template
from flask import redirect, url_for
from flask import flash

from dateutil.parser import parse

from app.models import User, Event

from app.forms import LoginForm, CreateUserForm
from app.forms import EventForm, EditUserForm
from flask_login import login_user, login_required, logout_user, current_user


@login_manager.user_loader
def user_loader(user_id):
    return User.query.get(user_id)


@app.errorhandler(404)
def page_not_found(e):
    title = "This page doesn't exist"
    return render_template('404.html', title=title), 404


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/events')
@login_required
def events():
    events = Event.query.order_by(Event.start_time).all()
    return render_template('events.html', events=events)


@app.route('/events/my')
@login_required
def my_events():
    events = Event.query.filter_by(
        author=current_user._id).order_by(Event.start_time)
    return render_template('events.html', events=events)


@app.route('/events/create/', methods=['GET', 'POST'])
@login_required
def event_create():
    form = EventForm()
    if request.method == "POST":
        if form.validate_on_submit():
            event = Event()
            event.author = current_user._id
            event.title = form.title.data
            event.text = form.text.data

            try:
                event.start_time = parse(form.start_time.data)

            try:
                event.end_time = parse(form.end_time.data)

            if event.end_time < event.start_time:
                event.end_time = event.start_time

            db.session.add(event)
            db.session.commit()
            return redirect(url_for('my_events'))
    return render_template('event_create.html', form=form)


@app.route('/events/edit/<int:_id>', methods=['GET', 'POST'])
@login_required
def event_edit(_id):
    event = Event.query.filter_by(_id=_id).first()
    form = EventForm()
    if current_user.email == event.user.email:
        if request.method == "POST":
            if event.title:
                event.title = form.title.data
            event.text = form.text.data

            try:
                event.start_time = parse(form.start_time.data)

            try:
                event.end_time = parse(form.end_time.data)

            if event.end_time < event.start_time:
                event.end_time = event.start_time

            db.session.add(event)
            db.session.commit()
            return redirect(f'/events/{_id}')

        if event:
            form.title.data = event.title
            form.text.data = event.text
            if event.start_time:
                form.start_time.data = event.start_time.strftime(
                    '%Y-%m-%d %H:%M:%S')
            if event.end_time:
                form.end_time.data = event.end_time.strftime(
                    '%Y-%m-%d %H:%M:%S')
            return render_template('event_edit.html', form=form)

    return redirect(url_for('events'))


@app.route('/events/<int:_id>')
@login_required
def event(_id):
    event = Event.query.filter_by(_id=_id).first()
    event._text = event.text.split('\n')
    return render_template('event.html', event=event)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            user = User.query.filter_by(email=form.email.data).first()
            print(user)
            if user.check_password(form.password.data):
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
def user():
    form = EditUserForm()
    if current_user.is_authenticated:

        if request.method == 'POST':
            print('POST')
            if form.validate_on_submit():
                user = User.query.filter_by(_id=current_user._id).first()
                if form.email.data:
                    user.email = form.email.data
                if form.username.data:
                    user.username = form.username.data
                db.session.commit()
                login_user(user, remember=True)
            return redirect(url_for('user'))

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
