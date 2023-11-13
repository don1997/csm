# tests/conftest.py
import pytest
from src.app import create_app, db
from src.app.models import User

@pytest.fixture(scope='module')
def test_app():
    """
    Create a Flask application configured for testing.
    """
    app = create_app()
    app.config.update({
        'TESTING': True,
        'SQLALCHEMY_DATABASE_URI': 'sqlite:///:memory:'  # Use in-memory SQLite database for testing.
    })

    # Create the database and the database table
    with app.app_context():
        db.create_all()

    yield app  # testing happens here

    with app.app_context():
        db.session.remove()
        db.drop_all()

@pytest.fixture(scope='module')
def client(test_app):
    return test_app.test_client()

@pytest.fixture(scope='module')
def new_user(test_app):
    """
    Create a user for the tests.
    """
    with test_app.app_context():
        user = User(username='testuser', password='testpassword')
        db.session.add(user)
        db.session.commit()
    return user
