# This is where you can start you Python file for your week1 web app - copied from sprint1
# Name: Jenna Gopilan

import flask, flask.views

users = {'jenna':'apple'}

class Login(flask.views.MethodView):
    def get(self):
        return flask.render_template('my_login.html')
    
    def post(self):
        if 'logout' in flask.request.form:
            flask.session.pop('username', None)
            return flask.redirect(flask.url_for('login'))
        required = ['username', 'passwd']
        for r in required:
            if r not in flask.request.form:
                flask.flash("Error: {0} is required.". format(r))
                return flask.redirect(flask.url_for('login'))
        username = flask.request.form['username']
        passwd = flask.request.form['passwd']
        if username in users and users[username] == passwd:
            flask.session['username'] = username
        else:
            flask.flash("Username doesn't exist or incorrect password")
        return flask.redirect(flask.url_for('login'))

