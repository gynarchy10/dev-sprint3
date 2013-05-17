# This is where you can start you Python file for your week1 web app - copied from sprint2
# Name: Jenna Gopilan

import flask
import settings

# Views
from index import Index
from contact import Contact
from about import About
from main import Main
from login import Login
from remote import Remote
from music import Music

app = flask.Flask(__name__)
app.secret_key = settings.secret_key

# Routes
app.add_url_rule('/',
                 view_func=Main.as_view('main'),
                 methods=["GET"])
app.add_url_rule('/about/',
                 view_func=About.as_view('about'),
                 methods=["GET"])
app.add_url_rule('/contact/',
                 view_func=Contact.as_view('contact'),
                 methods=["GET"])
app.add_url_rule('/index/',
                 view_func=Index.as_view('index'),
                 methods=["GET"])
app.add_url_rule('/<page>/',
                 view_func=Main.as_view('main'),
                 methods=["GET"])
app.add_url_rule('/login/',
                 view_func=Login.as_view('login'),
                 methods=["GET", "POST"])
app.add_url_rule('/remote/',
                 view_func=Remote.as_view('remote'),
                 methods=["GET", "POST"])
app.add_url_rule('/music/',
                 view_func=Music.as_view('music'),
                 methods=["GET"])

@app.errorhandler(404)
def page_not_found(error):
    return flask.render_template('my_404.html'), 404

app.debug = True
app.run()