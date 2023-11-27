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
def test_smoke(test_app,test_client):

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

    with patch('flask_login.utils._get_user') as current_user_mock:
        # Mock the current_user to simulate a logged-in state
        current_user_mock.return_value = User(id=1, username='testuser')
        response = test_client.get('/dashboard')
        assert response.status_code == 200
        assert b"LOGO" in response.data
        
        
        
        # Further assertions...
        # testing new snippet
       # response = client.get('/snippet/new')
      #  assert response.status_code == 200
      #  assert b"placeholder" in response.data

       # response = client.get('/logout')
       # assert response.statue_code == 200
       # assert b"Login Page" in response.data 
        
        
        
        #creating new snippet
        #testSnippet = Snippet(title = 'test', content = 'test code', author = current_user_mock)
        #db.session.add(testSnippet)
        #db.session.commit()

        #response = client.get('/snippet/<int:0>/edit')
        #assert response.status_code == 200
        
        #test delete snippet
        

    #testing 
