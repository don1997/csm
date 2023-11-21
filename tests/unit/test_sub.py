
from src.app.models import Snippet
def test_form_submission(client, db_session):
    # Given form data to submit
    form_data = {
        'title': 'New Snippet',
        'content': 'print("Hello, World!")',
        # Add any other form fields here
    }

    # When the form is submitted to the create snippet route
    response = client.post(url_for('create_snippet_route'), data=form_data)

    # Then the response should indicate a successful submission (e.g., a redirect)
    assert response.status_code == 302  # Assuming it redirects after successful submission

    # And the snippet should be added to the database
    snippet = Snippet.query.filter_by(title='New Snippet').first()
    assert snippet is not None
    assert snippet.content == 'print("Hello, World!")'

