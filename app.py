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

if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
mongo = PyMongo(app)
users = mongo.db.user


# Routes

# Render Homepage


@app.route("/")
@app.route("/home")
def home():
    return render_template('index.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if request.method == "POST":
        existing_user = users.find_one(
            {"username": form.username.data})
        if existing_user:
            if existing_user and check_password_hash(existing_user['password'],
                                                     form.password.data.encode()):
                flash("You have Logged in!")
                username = form.username.data
                session["user"] = username
                return redirect(url_for("profile", username=session["user"]))

        else:
            flash('incorrect login')
    return render_template("login.html", form=form)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegistrationForm()
    if request.method == "POST":
        existing_user = users.find_one(
            {"username": form.username.data})
        if existing_user:
            flash("That user name already exists")
            return redirect(url_for("login"))

        hash_password = generate_password_hash(
            form.password.data)

        register = {
            "username": form.username.data,
            "password": hash_password,
        }
        users.insert_one(register)
        username = form.username.data
        session["user"] = username

        flash(" Account registered!")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("signup.html", form=form)


@app.route("/dictionary")
def dictionary():
    dictionary = list(mongo.db.dictionary.find())
    return render_template("dictionary.html", dictionary=dictionary)


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    username = users.find_one(
        {"username": session["user"]})['username']

    if session["user"]:
        return render_template(
            "profile.html",
            username=username)

    return redirect(url_for("login"))


@ app.route("/contact")
def contact():
    return render_template('contact.html')


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
