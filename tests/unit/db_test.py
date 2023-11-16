from src.app.models import User

def test_add_and_retrieve_user(session):
    # Add a new user
    new_user = User(username='newuser', password='newpassword')
    session.add(new_user)
    session.commit()

    # Retrieve the added user
    retrieved_user = session.query(User).filter_by(username='newuser').first()
    
    print(f"Username {new_user.username}")
    print(f"PASS {new_user.password}")
    # Assert that the retrieved user matches the added user
    assert retrieved_user is not None
    assert retrieved_user.username == 'newuser'
    assert retrieved_user.password == 'newpassword'
    
