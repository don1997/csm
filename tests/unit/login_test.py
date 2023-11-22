from unittest.mock import patch
from src.app.models import User

"""
ISSUE: User auth was not letting me through to next page no matter what
SOL: Bypass User auth tried modify route but didn't work
FInal SOL: 
"""
        
def test_dashboard_access(client):
    with patch('flask_login.utils._get_user') as current_user_mock:
        # Mock the current_user to simulate a logged-in state
        current_user_mock.return_value = User(id=1, username='testuser')
        response = client.get('/dashboard')
        assert response.status_code == 200
        assert b"LOGO" in response.data
        # Further assertions...
        
        response = client.get('/snippet/new')

         
