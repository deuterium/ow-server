from app import app
from flask import render_template, url_for, flash, get_flashed_messages, request, redirect, abort, session, g
from flask_restful import Api
from app.objects import CVEProduct, CVEVendor, CVEID
from app.authentication import auth

api = Api(app)

api.add_resource(CVEVendor  , '/api/cve/vendor')
api.add_resource(CVEID      , '/api/cve/<string:cve_id>')
api.add_resource(CVEProduct , '/api/cve/product/<string:product_id>')

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
@auth.login_required
def about():
    return render_template("about.html")

