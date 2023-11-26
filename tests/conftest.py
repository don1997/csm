import pytest
from src.app import create_app, db
from src.app.models import User, Snippet, Tag
from datetime import datetime

@pytest.fixture(scope='module')
def test_app():
    app = create_app({
        'WTF_CSRF_ENABLED': False,  # Disable CSRF for testing
        'TESTING': True,
        'SQLALCHEMY_DATABASE_URI': 'sqlite:///test_database.db'
    })
    with app.app_context():
        yield app
        
        
@pytest.fixture(scope='module')
def test_db(test_app):
    db.create_all()

    yield db

    db.session.remove()
    db.drop_all()

@pytest.fixture(scope='module')
def test_client(test_app):
    return test_app.test_client()



@pytest.fixture(scope='function')
def new_user():
    user = User(username='testuser', password='testpassword')
    return user

@pytest.fixture(scope='function')
def new_snippet(new_user):
    snippet = Snippet(title='Test Snippet', content='Test content', author=new_user, date_posted=datetime.utcnow())
    return snippet

@pytest.fixture(scope='function')
def new_tag():
    tag = Tag(title='Test Tag')
    return tag

@pytest.fixture(scope='function')
def add_user(test_db, new_user):
    
    test_db.session.add(new_user)
    test_db.session.commit()
    return new_user

@pytest.fixture(scope='function')
def add_snippet(test_db, new_snippet):
    test_db.session.add(new_snippet)
    test_db.session.commit()
    return new_snippet

@pytest.fixture(scope='function')
def add_tag(test_db, new_tag):
    test_db.session.add(new_tag)
    test_db.session.commit()
    return new_tag
