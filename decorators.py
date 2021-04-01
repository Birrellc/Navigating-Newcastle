from functools import wraps
from flask import flash, redirect, url_for, session

# Function used by the Logged_in_required function to check if there is a user in session data
def user_logged_in():
    if session.get('user') is None:
        return False
    return True


# Login Decorator function used to return user to the login page if they try access another account which is not their own
def logged_in_required(func):
    @wraps(func)
    def route(*args, **kwargs):
        if user_logged_in():
            return func(*args, **kwargs)
        flash("You need to be logged in to view that!")
        return redirect(url_for("login"))
    return route
