import flask, flask.views
import os

class Index(flask.views.MethodView):
    def get(self, page="my_index"):
        page += ".html"
        if os.path.isfile('templates/' + page):
            return flask.render_template(page)
        flask.abort(404)
