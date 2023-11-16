import pytest


"""
allows for command $ pytest -m smoke 
for running
"""
@pytest.mark.smoke
def test_smoke():
    pass
