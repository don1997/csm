def test_home(client):
    """
    GIVEN Flask app
    WHEN the / is requested (GET) 
    THEN check the response is valid and check for the given strin
    """
    response = client.get('/')
    assert response.status_code == 200
    assert b"Login Authentication System in Flask." in response.data




