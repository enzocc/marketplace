"""Core database configuration."""
from flask_sqlalchemy import SQLAlchemy

from app.core.config import settings

# Global to hold database engine and session
db = SQLAlchemy()
# Base SQLAlchemy model
Base = db.Model


def connect_database(app, testing=False):
    """Called on app startup to connect the database.

    This will populate the global session/engine in _db.
    """
    if testing:
        settings.SQLALCHEMY_DATABASE_URI = "sqlite:////tmp/test.db"

    app.config.from_object(settings)
    db.init_app(app)
