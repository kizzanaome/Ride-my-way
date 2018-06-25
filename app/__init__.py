"""
third-party imports
"""
from flask import Flask, redirect, render_template, request, url_for
"""
common imports
"""
from instance.config import app_config

"""create_app function loads the correct configuration 
   from the config.py given a configuration name
"""

def create_app(config_name):
    app= Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')

    """
    Registering blueprints

    """

    from .rides import rides as rides_blueprints
    app.register_blueprint(rides_blueprints)

    @app.route("/")
    def index():
        return "hello index"
    return app