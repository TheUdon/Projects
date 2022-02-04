from werkzeug.security import generate_password_hash, check_password_hash
from flask import Flask, render_template, redirect, url_for, request, jsonify, flash
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm, Form
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
from wtforms import StringField, SubmitField, DateField, PasswordField
from wtforms.validators import DataRequired, Email
import random
from flask_sqlalchemy import SQLAlchemy
from typing import Callable
import datetime as dt
import sqlite3

# First time set up
# db = sqlite3.connect("ToDoList.db")
# cursor = db.cursor()
# cursor.execute("CREATE TABLE tasks (id INTEGER PRIMARY KEY, user varchar(250) NOT NULL, task_name varchar(250) NOT NULL, due_date varchar(250) NULL, priority INTEGER NULL, note varchar(500) NULL)")
# cursor.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, user varchar(250) NOT NULL UNIQUE, email varchar(250) NOT NULL, hash varchar(250) NOT NULL, salt varchar(250) NOT NULL)")
# db.commit()
app = Flask(__name__)

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user):
    return User.query.get(user)

##Connect to Database
app.config['SECRET_KEY'] = 'N6NnTBUUxTxrovGfBjEU'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ToDoList.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


class MySQLAlchemy(SQLAlchemy):
    Column: Callable
    String: Callable
    Integer: Callable
    Float: Callable
    Boolean: Callable


db = MySQLAlchemy(app)

Bootstrap(app)

##Task TABLE Configuration
class Task(db.Model):
    __tablename__='tasks'
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(250), nullable=False)
    task_name = db.Column(db.String(250), nullable=False)
    due_date = db.Column(db.String(500), nullable=True)
    note = db.Column(db.String(500), nullable=True)
    priority = db.Column(db.Integer, nullable=True)

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


class User(UserMixin, db.Model):
    __tablename__='users'
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(250), nullable=False)
    email = db.Column(db.String(250), nullable=False)
    hash = db.Column(db.String(500), nullable=False)
    salt = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}

# Forms
class CreateTaskForm(FlaskForm):
    task_name = StringField('What you need to do: ', validators=[DataRequired()])
    due_date = DateField('When you need to finish it by: ', validators=[DataRequired()])
    note = StringField('Any notes about this task? If none, leave blank.', render_kw={"placeholder": "N/A"})
    submit = SubmitField('Submit')


class SignUpForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Submit')


class LoginForm(FlaskForm):
    username = StringField("Username or Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Log In")

# Routes
@app.route("/")
def home():
    return render_template("index.html", logged_in=current_user.is_authenticated)


@app.route("/signup", methods=["GET", "POST"])
def signup():
    signup = SignUpForm()
    if signup.validate_on_submit():

        if User.query.filter_by(email=signup.email.data).first():
            flash("There is already an account with this email, log in instead")
            return redirect(url_for("signup"))

        username = signup.username.data
        hash_and_salt_passsword = generate_password_hash(
            signup.password.data,
            method="pbkdf2:sha256",
            salt_length=8
        )

        new_user = User(
            user=username,
            email=signup.email.data,
            hash=hash_and_salt_passsword,
            salt=8
        )

        db.session.add(new_user)
        db.session.commit()
        load_user(new_user)
        return redirect(url_for("user", user=new_user.user, logged_in=current_user.is_authenticated))
    return render_template("signup.html", form=signup)


@app.route("/login", methods=["GET", "POST"])
def login():
    login = LoginForm()
    if login.validate_on_submit():
        username = login.username.data
        password = login.password.data
        if username[:-4] == ".com":
            user = User.query.filter_by(email=username).first()
        else:
            user = User.query.filter_by(user=username).first()

        if user and check_password_hash(user.hash, password):
            login_user(user)
            username = user.user
            return redirect(url_for("user", user=username))
        elif not user:
            flash("That email or username doesn't exist, please try again")
            return redirect(url_for("login"))
        elif not check_password_hash(user.hash, password):
            flash("Password incorrect, please try again.")
            return redirect(url_for("login"))

    return render_template("login.html", form=login, logged_in=current_user.is_authenticated)


@app.route("/<user>", methods=["GET", "POST"])
def user(user):
    form = CreateTaskForm()
    if form.validate_on_submit():
        task = Task(
            user = user,
            task_name = form.task_name.data,
            due_date = form.due_date.data,
            note = form.note.data
        )
        db.session.add(task)
        db.session.commit()
        return redirect(url_for("tasks", user=user))
    return render_template("user_page.html", form=form, user=user)


@app.route("/<user>/tasks", methods=["GET", "POST"])
def tasks(user):
    all_tasks = Task.query.all()
    current_day = dt.datetime.strptime(str(dt.date.today()), '%Y-%m-%d').date()
    return render_template("tasks.html", tasks=all_tasks, user=user, current_day=current_day, dt=dt, str=str)


@app.route("/<user>/remove/<task_id>", methods=["GET", "POST"])
def remove(task_id, user):
    task_to_remove = Task.query.get(task_id)
    db.session.delete(task_to_remove)
    db.session.commit()
    all_tasks = Task.query.all()
    current_day = dt.datetime.strptime(str(dt.date.today()), '%Y-%m-%d').date()
    return render_template("tasks.html", tasks=all_tasks, user=user, current_day=current_day, dt=dt, str=str)


@app.route("/signout")
def signout():
    logout_user()
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)
