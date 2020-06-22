# built-in library
import os

# external library
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
bootstrap = Bootstrap()
login_manager = LoginManager()
login_manager.login_view = 'authentication.do_login'
login_manager.session_protection = 'strong'
bcrypt = Bcrypt()


def create_app(config_type):  # development, production, testing
    app = Flask(__name__)
    config_file = os.path.join(os.getcwd() + '\\config', config_type + '.py')
    app.config.from_pyfile(config_file)
    # initialise application wwith db instance
    db.init_app(app)
    # initialize bootstrap
    bootstrap.init_app(app)
    # initialize login manager
    login_manager.init_app(app)
    # initialize bcrypt
    bcrypt.init_app(app)

    # import and register your blueprint name to the instance of application
    from application.library import library
    from application.authentication import authentication
    app.register_blueprint(library)
    app.register_blueprint(authentication)

    return app
