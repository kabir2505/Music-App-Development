from flask import Blueprint
from flask_security import auth_required,roles_required

auth=Blueprint('auth',__name__)


@auth.route('/signup')
def signup():
    return '<p>signup</p>'


@auth.route('/login')
def login():
    return '<p>login</p>'



@auth.route('/logout')
def logout():
    return '<p>logout</p>'