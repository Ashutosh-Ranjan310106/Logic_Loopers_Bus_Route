import os,sys
sys.path.append(os.getcwd())
import pytest
from user_employee_app.app import app  # Import your Flask app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_user_creation(client):
    response = client.post('/user/create', json={
        'name': 'Test User',
        'email': 'test@example.com',
        'password': 'password123'
    })
    assert response.status_code == 409
    assert b'alredy' in response.data

def test_user_login(client):
    response = client.post('/user/login', json={
        'email': 'test@example.com',
        'password': 'password123'
    })
    assert response.status_code == 200
    assert b'success' in response.data

def test_fare_calculation(client):
    response = client.get('/user/fare?bus_number=DTC-427&starting_stop_number=1&ending_stop_number=5&category=red')
    assert response.status_code == 200
    assert b'fare' in response.data
