# This is where you can start you Python file for your week1 web app - copied from sprint2
# Name: Jenna Gopilan

import flask
import settings

# Views
from login import Login
from remote import Remote
from music import Music

app = flask.Flask(__name__)
app.secret_key = settings.secret_key

# Routes
app.add_url_rule('/',
                 view_func=Login.as_view('login',),
                 methods=["GET", "POST"])
app.add_url_rule('/login/',
                 view_func=Login.as_view('login'),
                 methods=["GET", "POST"])
app.add_url_rule('/remote/',
                 view_func=Remote.as_view('remote'),
                 methods=["GET", "POST"])
app.add_url_rule('/music/',
                 view_func=Music.as_view('music'),
                 methods=["GET"])

app.debug = True
app.run()