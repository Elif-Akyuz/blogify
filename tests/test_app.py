import pytest
from app import app, db, BlogPost

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client

def test_index_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Henüz yazı yok' in response.data or b'Blog Yazıları' in response.data

def test_healthcheck(client):
    response = client.get('/health')
    assert response.status_code == 200
    assert b'OK' in response.data

def test_add_post(client):
    response = client.post('/new', data=dict(title="Test Başlık", content="Test içerik"), follow_redirects=True)
    assert response.status_code == 200
    assert b'Test Başlık' in response.data
