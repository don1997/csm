from src.app.models import Snippet, User
# Integration testing
# Test diff parts of app and interactions between them

def test_user_registration_and_login_flow(test_app, test_client, test_db):
    # Test user registration
    registration_data = {'username': 'newuser', 'password': 'newpassword'}
    response = test_client.post('/register', data=registration_data, follow_redirects=True)
    assert response.status_code == 200

    # Test user login
    login_data = {'username': 'newuser', 'password': 'newpassword'}
    response = test_client.post('/login', data=login_data, follow_redirects=True)
    assert response.status_code == 200
    assert 'Dashboard' in response.data.decode('utf-8')
    
    response = test_client.post('/dashboard/new', follow_redirects=True)
    assert 'New Snippet' in response.data.decode('utf-8')
    
    response = test_client.post('/dashboard', follow_redirects=True)
    assert 'Dashboard' in response.data.decode('utf-8')

    response = test_client.post('/logout', follow_redirects=True)
    assert 'Login' in response.data.decode('utf-8')
    
    response = test_client.post('/login', data=login_data, follow_redirects=True)
    assert response.status_code == 200
    assert 'Dashboard' in response.data.decode('utf-8')
    
    response = test_client.post('/dashboard/new', follow_redirects=True)
    assert 'New Snippet' in response.data.decode('utf-8')

    snippet_data = {'title': 'snippet_title', 'content': 'aaa'}
    response = test_client.post('/dashboard', data=snippet_data, follow_redirects=True)
    
    assert 'Dashboard' in response.data.decode('utf-8')

    