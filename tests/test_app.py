import sys
import os
import pytest
from app import app

# Proje dizinini sys.path'e eklemek (gerekirse)
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_index(client):
    response = client.get('/')
    assert response.status_code == 200
    # Eğer 'posts' listesi boşsa, ana sayfada gösterilen metni kontrol et
    assert 'Henüz yazı yok' in response.data.decode('utf-8') or 'Post' in response.data.decode('utf-8')

def test_create_post(client):
    response = client.post('/new', data={'title': "Test Başlık", 'content': "Test içerik"}, follow_redirects=True)
    assert response.status_code == 200
    assert 'Test Başlık' in response.data.decode('utf-8')

def test_post_view(client):
    # Önce post oluştur
    client.post('/new', data={'title': "Yeni Post", 'content': "Detay içerik"}, follow_redirects=True)

    # Oluşturulan postu görüntüle
    response = client.get('/post/0')
    assert response.status_code == 200
    assert 'Yeni Post' in response.data.decode('utf-8')

def test_health_check(client):
    response = client.get('/health')
    assert response.status_code == 200
    assert response.data == b'OK'
