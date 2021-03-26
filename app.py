import os
from bson.objectid import ObjectId
from flask_pymongo import PyMongo
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from forms import (RegistrationForm,
                   LoginForm, DictionaryForm, UpdateWordForm, SearchForm)

if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
mongo = PyMongo(app)
users = mongo.db.user


# Login decorators


def user_logged_in():
    if session.get('user') is None:
        return False
    return True


def logged_in_required(func):
    @wraps(func)
    def route(*args, **kwargs):
        if user_logged_in():
            return func(*args, **kwargs)
        flash("You need to be logged in to view that!")
        return redirect(url_for("login"))
    return route


# Routes


@app.route("/")
@app.route("/home")
def home():
    return render_template('index.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit() and request.method == "POST":
        existing_user = users.find_one(
            {"username": form.username.data})
        if existing_user:
            if existing_user and check_password_hash(
                    existing_user['password'],
                    form.password.data.encode()):
                flash("You have Logged in!", "logged_in")
                username = form.username.data
                session["user"] = username
                return redirect(url_for("profile", username=session["user"]))

        else:
            flash('incorrect login details', "incorrect")
    return render_template("login.html", form=form)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegistrationForm()
    if form.validate_on_submit() and request.method == "POST":
        existing_user = users.find_one(
            {"username": form.username.data})
        if existing_user:
            flash("That user name already exists", "user_exists")
            return redirect(url_for("signup"))

        hash_password = generate_password_hash(
            form.password.data)

        register = {
            "username": form.username.data,
            "password": hash_password,
        }
        users.insert_one(register)
        username = form.username.data
        session["user"] = username

        flash(" Account registered!", "success")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("signup.html", form=form)


@app.route("/dictionary")
def dictionary():
    form = SearchForm()
    dictionary = list(mongo.db.dictionary.find())
    return render_template("dictionary.html", dictionary=dictionary, form=form)


@app.route("/profile/<username>", methods=["GET", "POST"])
@logged_in_required
def profile(username):
    username = users.find_one(
        {"username": session["user"]})['username']
    dictionary = list(mongo.db.dictionary.find())

    if session["user"]:
        return render_template(
            "profile.html",
            dictionary=dictionary, username=username)

    return redirect(url_for("login"))


@app.route("/add_word", methods=["GET", "POST"])
@logged_in_required
def add_word():
    form = DictionaryForm()
    if form.validate_on_submit():
        existing_word = mongo.db.dictionary.find_one(
            {"word": form.word.data})

        if existing_word:
            flash("Your word already exists", "word_exists")
            return redirect(url_for("add_word"))
        words = {
            "word": form.word.data,
            "definition": form.definition.data,
            "example": form.example.data,
            "added_by": session["user"]
        }
        mongo.db.dictionary.insert_one(words)
        flash("Your word is now in the dictionary", "word_added")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("add_word.html", form=form)


@app.route("/update_word/<word_id>", methods=["GET", "POST"])
@logged_in_required
def update_word(word_id):
    form = UpdateWordForm()
    word = mongo.db.dictionary.find_one({"_id": ObjectId(word_id)})
    dictionaries = mongo.db.dictionary.find().sort("word", 1)
    if form.validate_on_submit():
        update = {
            "word": form.word.data,
            "definition": form.definition.data,
            "example": form.example.data,
            "added_by": session["user"]
        }
        mongo.db.dictionary.update({"_id": ObjectId(word_id)}, update)
        flash("Your word is now in the dictionary", "updated_word")
    return render_template("update_word.html", form=form, word=word,
                           dictionaries=dictionaries)


@app.route("/delete_word/<word_id>")
@logged_in_required
def delete_word(word_id):
    mongo.db.dictionary.remove({"_id": ObjectId(word_id)})
    flash("Your word has been deleted", "deleted_word")
    return redirect(url_for("profile", username=session["user"]))


@app.route("/logout")
@logged_in_required
def logout():
    flash("You have been logged out!", "logged_out")
    session.pop("user")
    return redirect(url_for("login"))


@ app.route("/contact")
def contact():
    return render_template('contact.html')


@ app.route("/search", methods=["GET", "POST"])
def search():
    form = SearchForm()
    if form.validate_on_submit() and request.method == "POST":
        query = form.word.data
        print(query)
        words = list(mongo.db.dictionary.find({"$text": {"$search": query}}))
        return render_template("dictionary.html", dictionary=words,
                               form=form, query=query)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
