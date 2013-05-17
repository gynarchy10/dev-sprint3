import flask, flask.views
import os

class Contact(flask.views.MethodView):
    def get(self, page="my_contact"):
        page += ".html"
        if os.path.isfile('templates/' + page):
            return flask.render_template(page)
        flask.abort(404)
