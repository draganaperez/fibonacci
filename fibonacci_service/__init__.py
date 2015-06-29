from flask import Flask
from flask.ext import restful


def create_fibonacci_app(app_name=__name__, debug=True):
    app = Flask(app_name)
    app.debug = debug
    return app


app = create_fibonacci_app()
api = restful.Api(app)
import fibonacci_service.resources  # NOQA
