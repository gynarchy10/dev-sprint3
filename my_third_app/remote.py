# This is where you can start you Python file for your week1 web app - copied from sprint1
# Name: Jenna Gopilan

import flask, flask.views
import os
import utils

class Remote(flask.views.MethodView):
    @utils.login_required
    def get(self):
        return flask.render_template('my_remote.html')
    
    @utils.login_required
    def post(self):
        result = eval(flask.request.form['expression'])
        flask.flash(result)
        return flask.redirect(flask.url_for('remote'))

