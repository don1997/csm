from flask_sqlalchemy import SQLAlchemy

class TestConfig:
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'  # Use an in-memory SQLite database for tests
    SECRET_KEY = 'test_secret_key'
    WTF_CSRF_ENABLED = False  # Disable CSRF tokens in the forms for testing purposes
    SQLALCHEMY_TRACK_MODIFICATIONS = False
