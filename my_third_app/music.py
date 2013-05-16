# This is where you can start you Python file for your week1 web app - copied from sprint1
# Name: Jenna Gopilan

import flask, flask.views
import os
import utils


class Music(flask.views.MethodView):
    @utils.login_required
    def get(self):
        songs = os.listdir('static/music/')
        return flask.render_template('my_music.html', songs=songs)
  