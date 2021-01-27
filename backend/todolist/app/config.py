
from os import path, environ

class Config:
    """Set Flask configuration from .env file"""

    # General Configurations
    FLASK_APP = environ.get('FLASK_APP')
    FLASK_ENV = environ.get('FLASK_ENV')

    # Database
    SQLALCHEMY_DATABASE_URI = 'postgresql://' + environ["POSTGRES_USERNAME"] + ':' + environ["POSTGRES_PASSWORD"] + '@' + environ["POSTGRES_HOST"] + '/' + environ["POSTGRES_DATABASE"]
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False