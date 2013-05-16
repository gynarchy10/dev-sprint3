# This is where you can start you Python file for your week1 web app - copied from sprint1
# Name: Jenna Gopilan

import flask
import functools

def login_required(method):
    @functools.wraps(method)
    def wrapper(*args, **kwargs):
        if 'username' in flask.session:
            return method(*args, **kwargs)
        else:
            flask.flash("A login is required to see the page!")
            return flask.redirect(flask.url_for('index'))
    return wrapper
