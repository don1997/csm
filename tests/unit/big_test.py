from src.app.forms import RegisterForm
from werkzeug.datastructures import MultiDict

def test_form_instantiation(test_app):
    with test_app.test_request_context():
        form = RegisterForm()
        assert form is not None
        
        
def test_valid_registration(test_app):
    with test_app.test_request_context():
        form_data = MultiDict([
            ('username', 'newuser'),
            ('password', 'securepassword123')
        ])
        form = RegisterForm(formdata=form_data)
        assert form.validate(), form.errors
        
        
def test_invalid_registration_username_too_short(test_app):
    with test_app.test_request_context():
        form_data = MultiDict([
            ('username', 'usr'),  # Less than 4 characters
            ('password', 'securepassword123')
        ])
        form = RegisterForm(formdata=form_data)
        assert not form.validate(), form.errors


def test_invalid_registration_password_too_short(test_app):
    with test_app.test_request_context():
        form_data = MultiDict([
            ('username', 'newuser'),
            ('password', 'short')  # Less than 8 characters
        ])
        form = RegisterForm(formdata=form_data)
        assert not form.validate(), form.errors
