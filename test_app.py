import pytest
from app import app

# Setting up the function for tests
@pytest.fixture
def client():
    app.testing = True # Activating the test mode for flask
    return app.test_client() # test client 


def test_home_page(client):
    """Test if the home page loads correctly and contains a working link to the About page."""
    response = client.get('/')
    assert response.status_code == 200
    assert b"Welcome to the Home Page" in response.data
    assert b'<a href="/about">' in response.data  # Check if the About page link is present

    # Follow the link
    response = client.get('/about')
    assert response.status_code == 200
    assert b"About Page" in response.data


def test_about_page(client):
    """Test if the About page loads correctly and contains a working link back to Home."""
    response = client.get('/about')
    assert response.status_code == 200
    assert b"About Page" in response.data
    assert b'<a href="/">' in response.data  # Check if the Home page link is present

    # Follow the link
    response = client.get('/')
    assert response.status_code == 200
    assert b"Welcome to the Home Page" in response.data
    