from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api

from config import config

db = SQLAlchemy()
api = Api()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    db.init_app(app)
    api.init_app(app)

    #api
    from .api import rest as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api/')

    return app
