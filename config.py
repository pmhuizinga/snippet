import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
    #                           'mssql://DESKTOP-DB7OB87\SQLPMH/CRUD?driver=SQL+Server'

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    """
    Development configurations
    """

    DEBUG = True
    SQLALCHEMY_ECHO = True

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'mssql://DESKTOP-DB7OB87\SQLPMH/CRUD?driver=SQL+Server'

class ProductionConfig(Config):
    """
    Production configurations
    """

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'mssql://DESKTOP-DB7OB87\SQLPMH/CRUD?driver=SQL+Server'

    DEBUG = False

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}