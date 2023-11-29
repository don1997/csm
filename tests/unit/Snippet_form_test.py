from src.app.forms import SnippetForm

from werkzeug.datastructures import MultiDict
"""
Form Max size input
"""

# Test normal form
# Needs werkzeug dict to work.
# Otherwise form will not be filled out with 
""" 
    form_data = {'title': 'Valid Title', 'content': 'a' * 500}
    form = SnippetForm(data=form_data)
    
"""

def test_snippet_form_content_length(test_app):
    form_data = MultiDict([
        ('title', 'Valid Title'), 
        ('content', 'a' * 500)
    ])
    form = SnippetForm(formdata=form_data)
    assert form.validate(), form.errors
    
    
def test_snippet_title_too_long(test_app):
    form_data = MultiDict([
        ('title', 'a' * 500), 
        ('content', 'a' * 500)
    ])
    form = SnippetForm(formdata=form_data)
    assert not form.validate(), form.errors



# 5 x10^10 causes failure: Memory Error
def test_snippet_content_limit_test(test_app):
    form_data = MultiDict([
        ('title', 'valid_title'), 
        ('content', 'a' * 4000001)
    ])
    form = SnippetForm(formdata=form_data)
    assert not form.validate(), form.errors
    
    