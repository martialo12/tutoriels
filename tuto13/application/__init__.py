# built-in library
import os

# external library
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def create_app(config_type):  # development, production, testing
    app = Flask(__name__)
    config_file = os.path.join(os.getcwd() + '\\config', config_type + '.py')
    app.config.from_pyfile(config_file)
    # initialise application wwith db instance
    db.init_app(app)

    # import and register your blueprint name to the instance of application
    from tuto13.application.library import library
    app.register_blueprint(library)

    return app
