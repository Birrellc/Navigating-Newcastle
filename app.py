from bson.objectid import ObjectId
from flask_pymongo import PyMongo
from werkzeug.security import generate_password_hash, check_password_hash
import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from forms import RegistrationForm, LoginForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
mongo = PyMongo(app)
users = mongo.db.user

login_manager = LoginManager()
login_manager.init_app(app)


# Forms

# Code used for this class below is credited to https://pythonprogramming.net/flask-user-registration-form-tutorial/


# class

class User(UserMixin):
    def __init__(self, user):
        self.user = user
        self.username = user['username']
        self.id = user['_id']
        self.email = user['email']
        self.password = user['password']

    def get_id(self):
        object_id = self.user['_id']
        return str(object_id)


@login_manager.user_loader
def load_user(user_id):
    user = users.find_one({'_id': ObjectId(user_id)})
    return User(user)


# Routes

# Render Homepage


@app.route("/")
@app.route("/home")
def home():
    return render_template('index.html')


@app.route("/signup", methods=["GET", "POST"])
def signup():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!')
        return redirect(url_for('home'))
    return render_template("signup.html", title="Signup", form=form)


@ app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'test@test.com' and form.password.data == 'password':
            flash('You are logged in!')
            return redirect(url_for('home'))
        else:
            flash('login unsucessful, please check credentials!')
    return render_template('login.html', title="Login", form=form)


@ app.route("/dictionary")
def dictionary():
    dictionary = list(mongo.db.dictionary.find())
    return render_template("dictionary.html", dictionary=dictionary)


@ app.route("/profile")
def profile():
    return render_template('profile.html')


@ app.route("/contact")
def contact():
    return render_template('contact.html')


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
