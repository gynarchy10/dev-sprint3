import flask, flask.views
import os

class About(flask.views.MethodView):
    def get(self, page="my_about"):
        page += ".html"
        if os.path.isfile('templates/' + page):
            return flask.render_template(page)
        flask.abort(404)
