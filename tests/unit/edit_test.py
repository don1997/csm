from src.app.models import Snippet
def test_edit_snippet(app, client, user, snippet):
    # Login as the test user
    client.login(user.username, 'test_password')

    # Edit the snippet
    response = client.post('/dashboard/1/edit', data={'title': 'Updated Title', 'content': 'Updated content'})

    # Assert that the snippet was updated
    assert response.status_code == 302
    assert Snippet.query.get(1).title == 'Updated Title'
    assert Snippet.query.get(1).content == 'Updated content'