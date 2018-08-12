from app import app
from functools import wraps
from flask import render_template, url_for, flash, get_flashed_messages, request, redirect, abort, session, g

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not ValidToken(session.get('loginToken')):
            #redirect to login page
            print("login_required decorater")
        return f(*args, **kwargs)
    return decorated_function

def ValidToken(t):
    if t is None:
        print("BLANK TOKEN")
        return False
    elif t is "testtoken":
        print("GOOD TOKEN")
        return True
    else:
        print("BAD TOKEN")
        return False

# # Create a user to test with
# @app.before_first_request
# def create_user():

@app.route('/')
def hello():
    return render_template("test.html")

@app.route('/about')
@login_required
def about():
    return render_template("about.html")

