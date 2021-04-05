import os
from bson.objectid import ObjectId
from flask_pymongo import PyMongo
from werkzeug.security import generate_password_hash, check_password_hash
from decorators import user_logged_in, logged_in_required
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
dict = mongo.db.dictionary


# Routes

# Home Route
@app.route("/")
@app.route("/home")
def home():
    return render_template('index.html')


# Login Route
@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit() and request.method == "POST":
        existing_user = users.find_one(
            {"username": form.username.data.lower()})
        if existing_user:
            if existing_user and check_password_hash(
                    existing_user['password'],
                    form.password.data.encode()):
                flash("You have Logged in!", "logged_in")
                username = form.username.data.lower()
                session["user"] = username
                return redirect(url_for("profile", username=session["user"]))
        flash('Incorrect login details', "incorrect")
    return render_template("login.html", form=form)


# Signup Route
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegistrationForm()
    if form.validate_on_submit() and request.method == "POST":
        existing_user = users.find_one(
            {"username": form.username.data.lower()})
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


# Logout Route
@app.route("/logout")
@logged_in_required
def logout():
    flash("You have been logged out!", "logged_out")
    session.pop("user")
    return redirect(url_for("login"))


# Dictionary Route
@app.route("/dictionary")
def dictionary():
    form = SearchForm()
    dictionary = list(dict.find())
    return render_template("dictionary.html", dictionary=dictionary, form=form)


# Profile Route
@app.route("/profile/<username>", methods=["GET", "POST"])
@logged_in_required
def profile(username):
    username = users.find_one(
        {"username": session["user"]})['username']
    dictionary = list(dict.find())

    if session["user"]:
        return render_template(
            "profile.html",
            dictionary=dictionary, username=username)

    return redirect(url_for("login"))


# Add Word Route
@app.route("/add_word", methods=["GET", "POST"])
@logged_in_required
def add_word():
    form = DictionaryForm()
    if form.validate_on_submit() and request.method == "POST":
        existing_word = dict.find_one(
            {"word": form.word.data.capitalize()})

        if existing_word:
            flash("Your word already exists", "word_exists")
            return redirect(url_for("add_word"))
        words = {
            "word": form.word.data.capitalize(),
            "definition": form.definition.data.capitalize(),
            "example": form.example.data.capitalize(),
            "added_by": session["user"]
        }
        dict.insert_one(words)
        flash("Your word is now in the dictionary", "word_added")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("add_word.html", form=form)


# Update Word Route
@app.route("/update_word/<word_id>", methods=["GET", "POST"])
@logged_in_required
def update_word(word_id):
    form = UpdateWordForm()
    word = dict.find_one({"_id": ObjectId(word_id)})
    dictionaries = dict.find().sort("word", 1)
    if form.validate_on_submit() and request.method == "POST":
        update = {
            "word": form.word.data.capitalize(),
            "definition": form.definition.data.capitalize(),
            "example": form.example.data.capitalize(),
            "added_by": session["user"]
        }
        dict.update({"_id": ObjectId(word_id)}, update)
        flash("Your word is now in the dictionary", "updated_word")
        return redirect(url_for("profile", username=session["user"]))
    return render_template("update_word.html", form=form, word=word,
                           dictionaries=dictionaries)


# Delete Word Route
@app.route("/delete_word/<word_id>")
@logged_in_required
def delete_word(word_id):
    dict.remove({"_id": ObjectId(word_id)})
    flash("Your word has been deleted", "deleted_word")
    return redirect(url_for("profile", username=session["user"]))


# Search Route
@ app.route("/search", methods=["GET", "POST"])
def search():
    form = SearchForm()
    if form.validate_on_submit() and request.method == "POST":
        query = form.word.data
        print(query)
        words = list(dict.find({"$text": {"$search": query}}))
        return render_template("dictionary.html", dictionary=words,
                               form=form, query=query)
# Error Handlers


# This error handler is a backup incase Login Decorator ever stops working
@app.errorhandler(403)
def page_forbidden(e):
    return render_template("403.html"), 403


# Renders a page not found error page
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


# Renders an internal server error page
@app.errorhandler(500)
def internal_server_error(e):
    return render_template("500.html"), 500


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)
