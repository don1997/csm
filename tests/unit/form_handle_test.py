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
