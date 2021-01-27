from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from .config import Config

db = SQLAlchemy()

def create_app():
    """Construct the core application"""
    app_flask = Flask(__name__, instance_relative_config=False)
    app_flask.config.from_object(Config)
    
    db.init_app(app_flask)

    with app_flask.app_context():
        import app.routes # Import routes
        db.create_all() # Create SQL tables for our data models
        print(type(app_flask))
        return app_flask