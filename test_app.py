import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_get_tasks_empty(client):
    response = client.get('/tasks')
    assert response.status_code == 200
    assert response.get_json() == []

def test_add_task(client):
    response = client.post('/tasks',
        json={'title': 'Test task'})
    assert response.status_code == 201
    assert response.get_json()['title'] == 'Test task'

def test_delete_task(client):
    client.post('/tasks', json={'title': 'To delete'})
    response = client.delete('/tasks/1')
    assert response.status_code == 200