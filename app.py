import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


# Forms

class LoginForm(FlaskForm):
    username = StringField('Username')
    email = StringField('Email')
    password = StringField('Password')
    submit = SubmitField(label="Sign Up")

# Routes

# Render Homepage

@app.route("/")
@app.route("/home")
def home():
    return render_template('index.html')


@app.route("/signup")
def signup():
    signup_form = LoginForm()
    return render_template('signup.html', form=signup_form)


@app.route("/login")
def login():
    return render_template('login.html')


@app.route("/dictionary")
def dictionary():
    dictionary = list(mongo.db.dictionary.find())
    return render_template("dictionary.html", dictionary=dictionary)


@app.route("/profile")
def profile():
    return render_template('profile.html')


@app.route("/contact")
def contact():
    return render_template('contact.html')


if __name__ =="__main__":
    app.run(host=os.environ.get("IP"),
    port=int(os.environ.get("PORT")),
    debug=True)