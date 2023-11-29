import pytest
from unittest.mock import patch
from src.app.models import User
from src.app.models import Snippet
from src.app import db
"""
allows for command $ pytest -m smoke 
for running
"""
@pytest.mark.smoke
def test_smoke(test_app,test_client,test_db):

    # testing home page
    response = test_client.get('/')
    assert response.status_code == 200
    assert b"Welcome" in response.data

    # testing login
    response = test_client.get('/login')
    assert response.status_code == 200
    assert b"Login" in response.data

    # testing register
    response = test_client.get('/register')
    assert response.status_code == 200
    assert b"Register"
    
     # Create and insert a mock user and snippet
    user = User(username='testuser', password='testpassword')
    test_db.session.add(user)
    test_db.session.commit()

    snippet = Snippet(title='Test Snippet', content='Test Content', author=user)
    test_db.session.add(snippet)
    test_db.session.commit()
    
    snippet_id = snippet.id
    with patch('flask_login.utils._get_user') as current_user_mock:
        # Mock the current_user to simulate a logged-in state
        current_user_mock.return_value = user
        response = test_client.get('/dashboard')
        assert response.status_code == 200
        assert b"LOGO" in response.data
        
        # Test accessing the new snippet form
        response = test_client.get('/dashboard/new')
        assert response.status_code == 200
        assert b"New Snippet" in response.data 
        
        response = test_client.get(f'/dashboard/{snippet_id}/edit')
        assert response.status_code == 200
        assert b"Edit Snippet" in response.data
        
        response = test_client.get(f'/dashboard/{snippet_id}/delete', follow_redirects=True)
        assert response.status_code == 200
        response = test_client.get('/dashboard')
        assert response.status_code == 200
        assert b"LOGO" in response.data