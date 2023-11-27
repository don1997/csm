from src.app.forms import RegisterForm, LoginForm
from src.app.models import User
from werkzeug.datastructures import MultiDict

def test_form_instantiation(test_app):
    with test_app.test_request_context():
        form = RegisterForm()
        assert form is not None
        
def test_valid_registration(test_app, test_db):
    with test_app.test_request_context():
        test_db.create_all()  # Ensure this is called
        form_data = MultiDict([
            ('username', 'newuser'), ('password', 'securepassword123') ])
        form = RegisterForm(formdata=form_data)
        assert form.validate(), form.errors

def test_invalid_registration_password_too_short(test_app,test_db):
    with test_app.test_request_context():
        test_db.create_all()  # Ensure this is called

        form_data = MultiDict([
            ('username', 'newuser'),
            ('password', 'short')  # Less than 8 characters
        ])
        form = RegisterForm(formdata=form_data)
        assert not form.validate(), form.errors
        
        
def test_valid_login(test_app,test_db):
    with test_app.test_request_context():
        test_db.create_all()  # Ensure this is called
        hashed_password = generate_password_hash('validpassword')
        user = User(username='validuser', password=hashed_password)
        test_db.session.add(user)
        test_db.session.commit()
        
        
        form_data = MultiDict([
            ('username', 'validuser'),
            ('password', 'validpassword')
        ])
        form = LoginForm(formdata=form_data)
        assert form.validate(), form.errors
        
        
from flask_bcrypt import generate_password_hash

def test_invalid_login_incorrect_password(test_app,test_db):
    with test_app.test_request_context():
        test_db.create_all()  # Ensure this is called
      
        hashed_password = generate_password_hash('correctpassword')
        user = User(username='validuser2', password=hashed_password)
        test_db.session.add(user)
        test_db.session.commit()

        form_data = MultiDict([
            ('username', 'validuser2'),
            ('password', 'wrongpassword')
        ])
        form = LoginForm(formdata=form_data)
        assert not form.validate(), form.errors
        
def test_invalid_login_empty(test_app,test_db):
    with test_app.test_request_context():
        test_db.create_all()  # Ensure this is called
        form_data = MultiDict([
            ('username', ''),
            ('password', '')
        ])
        form = LoginForm(formdata=form_data)
        assert not form.validate(), form.errors


from src.app.models import Snippet
def snippet_creation_test(test_app, test_db):
    # Setup: Create two users and a snippet
    with test_app.test_request_context():
    
        test_db.create_all()  # Ensure this is called

        user1 = User(username='user1', password='password1')
        snippet = Snippet(title='Test Snippet', content='Initial Content', author=user1)
        test_db.session.add_all([user1, snippet])
        test_db.session.commit()

        assert snippet.title == 'Test Snippet'
        assert snippet.title == 'Initial Content'

