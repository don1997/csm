"""
Form Testing
"""
from src.app.forms import SnippetForm, LoginForm
def test_form_handle(test_app, test_client, test_db):
    # Test user registration
    registration_data = {'username': 'newuser', 'password': 'newpassword'}
    response = test_client.post('/register', data=registration_data, follow_redirects=True)
    assert response.status_code == 200

    # Test user login
    login_data = {'username': 'newuser', 'password': 'newpassword'}
    response = test_client.post('/login', data=login_data, follow_redirects=True)
    assert response.status_code == 200
    assert 'Dashboard' in response.data.decode('utf-8')
    # In dash
    response = test_client.post('/dashboard/new',follow_redirects=True)
    # In new snippet
    assert 'Snippet Title!' in response.data.decode('utf-8')
    
    ## TODO
    snippet_data = {'title': 'a' * 500  , 'content': 'newpassword'}
    response = test_client.post('/dashboard/new',data=snippet_data, follow_redirects=True)

    assert 'Dashboard' in response.data.decode('utf-8')

from werkzeug.datastructures import MultiDict
from src.app.forms import RegisterForm
def test_reg_name_long(test_app, test_db):
    with test_app.test_request_context():
        test_db.create_all()  # Ensure this is called
        form_data = MultiDict([
            ('username', 'Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean m'), ('password', 'securepassword123') ])
        form = RegisterForm(formdata=form_data)
        assert not form.validate(), form.errors
