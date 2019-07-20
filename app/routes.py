from app import app, db, admin
from flask import render_template, url_for, redirect, flash
from app.forms import LoginForm, RegisterForm
from app.models import User
from flask_login import current_user, login_user, logout_user, login_required
from flask_admin.contrib.sqla import ModelView

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Index')

@app.route('/who')
def who():
    return render_template('who.html', title='Who We Are')

@app.route('/what')
def what():
    return render_template('what.html', title='What We Do')

@app.route('/where')
def where():
    return render_template('where.html', title='Where We Work')

@app.route('/contact')
def contact():
    return render_template('contact.html', title='Contact Us')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        flash('You are already logged in.')
        return redirect(url_for('index'))

    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()

        if user is None or not user.check_password(form.password.data):
            flash('Credentials are incorrect.')
            return redirect(url_for('login'))

        login_user(user, remember=form.remember_me.data)
        flash('You are now logged in.')
        return redirect(url_for('index'))

    return render_template('form.html', form=form, title='Login')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        flash('You are already logged in.')

    form = RegisterForm()

    if form.validate_on_submit():
        user = User(
            first_name = form.first_name.data,
            last_name = form.last_name.data,
            username = form.username.data,
            email = form.email.data
        )

        user.set_password(form.password.data)

        db.session.add(user)
        db.session.commit()

        flash('Thanks for registering!')
        return redirect(url_for('login'))

    return render_template('form.html', form=form, title='Register')

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

admin.add_view(ModelView(User, db.session))
