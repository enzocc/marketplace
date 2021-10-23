"""Reusable fixtures."""
# mypy: no-disallow-untyped-decorators
import os
from typing import Generator

import pytest

from app.api import create_app
from app.models import db, Products
from app.core.database import connect_database


@pytest.fixture(scope="module")
def test_app() -> Generator:
    """Test app.

    Yields:
        Generator: App for testing.
    """
    # Here we connect a sqlite database for quick tests
    app = create_app()
    connect_database(app, testing=True)

    with app.app_context():
        db.create_all()

    try:
        yield app
    finally:
        try:
            os.remove("/tmp/test.db")
        except OSError:
            pass


@pytest.fixture(scope="module")
def client(test_app) -> Generator:
    """Testing client.

    Yields:
        Generator: Client for testing.
    """
    with test_app.test_client() as client:
        yield client
