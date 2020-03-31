from flask import render_template, request, flash, redirect, url_for
from flask_login import login_user, login_required, logout_user, current_user

from application.authentication.forms import RegistrationForm, LoginForm
from application.authentication import authentication as auth
from application.authentication.models import User


@auth.route('/register', methods=['GET', 'POST'])
def register_user():
    if current_user.is_authenticated:
        flash('You are already logged-in')
        return redirect(url_for('library.display_books'))
    form = RegistrationForm()

    if form.validate_on_submit():
        User.create_user(
            user=form.name.data,
            email=form.email.data,
            password=form.password.data
        )
        flash('Registration Successful')
        return redirect(url_for('authentication.do_login'))
    return render_template('registration.html', form=form)


@auth.route('/login', methods=['GET', 'POST'])
def do_login():
    if current_user.is_authenticated:
        flash('You are already logged-in')
        return redirect(url_for('library.display_books'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(user_email=form.email.data).first()
        if not user or not user.check_password(form.password.data):
            flash('Invalid credentials, please try again!')
            return redirect(url_for('authentication.do_login'))

        login_user(user, form.stay_loggedin.data)
        return redirect(url_for('library.display_books'))

    return render_template('login.html', form=form)


@auth.route('/logout')
@login_required
def do_logout():
    logout_user()
    return redirect(url_for('library.display_books'))


@auth.app_errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404
