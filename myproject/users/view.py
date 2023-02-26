# users/view.py

from flask import render_template, redirect, url_for, flash, request, Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from myproject import db
from myproject.models import Users, JKSarees
from myproject.users.forms import RegistrationForm, LoginForm


users = Blueprint('users', __name__)

""""""
#register
@users.route('/register', methods=['GET','POST'])
def register():

    form = RegistrationForm()

    if form.validate_on_submit():
        user = Users(username=form.username.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Thanks for registering!!')
        return redirect(url_for('users.login'))
    return render_template('register.html', form=form)


# login
@users.route("/login", methods=['GET', 'POST'])
def login():

    form = LoginForm()

    if form.validate_on_submit():

        user = Users.query.filter_by(username = form.username.data).first()
        if user is None:
            flash("User name doesn't exists")

            return render_template('login.html', form=form)
        print(form.password.data)
        if user.check_password(form.password.data) and user is not None:
            
            login_user(user)
            flash('Log in success')

            next = request.args.get('next')

            if next == None or not next[0] == '/':
                next = url_for('core.home')
            
            return redirect(next)
    return render_template('login.html', form=form)




#logout
@users.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('core.home'))
