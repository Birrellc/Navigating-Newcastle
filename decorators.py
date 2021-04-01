from functools import wraps
from flask import flash, redirect, url_for, session


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
