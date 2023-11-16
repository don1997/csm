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

from src.app import bcrypt

@pytest.fixture(scope='module')
def new_user(test_app):
    """
    Create a user for the tests with a plain text password.
    """
    with test_app.app_context():
        user = User(username='testuser', password='testpassword')
        db.session.add(user)
        db.session.commit()
        return user
    
@pytest.fixture(scope='function')
def session(test_app):
    """Provides an isolated database session for each test."""
    # Push an application context to bind the SQLAlchemy object to your app
    context = test_app.app_context()
    context.push()

    connection = db.engine.connect()
    transaction = connection.begin()

    options = dict(bind=connection, binds={})
    session = db.create_scoped_session(options=options)

    db.session = session

    yield session

    session.remove()
    transaction.rollback()
    connection.close()

    context.pop()
