import pytest
import sys
import os

# Add the app directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../app')))

from app import app  # Import the Flask app
print("App object:", app)  # Add this line to debug

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_get_performance(client):
    response = client.get('/performance')
    assert response.status_code == 200
    assert isinstance(response.get_json(), list)

def test_add_performance(client):
    data = {"employee_name": "John Doe", "evaluation": "Excellent"}
    response = client.post('/performance', json=data)
    assert response.status_code == 200
    assert response.get_json() == {"message": "Performance data added successfully"}