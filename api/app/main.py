from app.api import create_app
from app.core.database import connect_database


def __getattr__(app):
    app = create_app()
    connect_database(app)
    return app
