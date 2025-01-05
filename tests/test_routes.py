import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    with app.test_client() as client:
        yield client

def test_get_performance_empty(client):
    response = client.get('/performance')
    assert response.status_code == 200  # Status code should be 200
    assert len(response.json) == 0  # No data in the database initially

def test_add_performance(client):
    data = {'employee_name': 'John Doe', 'evaluation': 'Excellent'}
    response = client.post('/performance', json=data)
    assert response.status_code == 201  # Status code should be 201 for successful POST
    assert response.json['message'] == "Performance data added successfully"

def test_get_performance_with_data(client):
    data = {'employee_name': 'Jane Doe', 'evaluation': 'Good'}
    client.post('/performance', json=data)  # Add data
    response = client.get('/performance')
    assert response.status_code == 200  # Status code should be 200
    assert len(response.json) == 1  # One entry in the database
    assert response.json[0]["employee_name"] == "Jane Doe"  # Ensure data matches
