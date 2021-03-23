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


@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')


@app.route('/signup')
def signup():
    return render_template('signup.html')


@app.route("/dictionary")
def dictionary():
    dictionary = list(mongo.db.dictionary.find())
    return render_template("dictionary.html", dictionary=dictionary)


@app.route("/profile", methods=["GET", "POST"])
def profile():
    return render_template('profile.html')


@ app.route("/contact")
def contact():
    return render_template('contact.html')


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
