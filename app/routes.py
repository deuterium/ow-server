from app import app
from flask import render_template, url_for, flash, get_flashed_messages, request, redirect, abort, session

@app.route('/')
def hello():
    return render_template("test.html")

@app.route('/about')
def about():
    return render_template("about.html")
