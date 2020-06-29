from flask import Flask
from config import config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
# app = Flask(__name__)
# app.config.from_object(Config)
# db = SQLAlchemy(app)
# migrate = Migrate(app, db)

# from app import models

def create_app(config_name='default'):

    app = Flask(__name__)
    # app.config.from_object(Config)
    app.config.from_object(config[config_name])
    # db = SQLAlchemy(app)
    db.init_app(app)
    migrate = Migrate(app, db)

    from .home import home as home_blueprint
    app.register_blueprint(home_blueprint, url_prefix="/home")
    print('Create app successfull')

    return app