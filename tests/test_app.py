import sys
import os
from app import app


sys.path.insert(
    0,
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), '..')
    )
)


def test_index():
    tester = app.test_client()
    response = tester.get('/')
    assert response.status_code == 200
    assert 'Henüz yazı yok' in response.data.decode('utf-8')


def test_create_post():
    tester = app.test_client()
    response = tester.post(
        '/new',
        data=dict(title="Test Başlık", content="Test içerik"),
        follow_redirects=True
    )
    assert response.status_code == 200
    assert 'Test Başlık' in response.data.decode('utf-8')


def test_post_view():
    tester = app.test_client()
    response = tester.post(
        '/new',
        data=dict(title="Yeni Post", content="Detay içerik"),
        follow_redirects=False
    )

    location = response.headers['Location']  
    post_id = location.split('/post/')[-1]

    response = tester.get(f'/post/{post_id}')
    assert response.status_code == 200
    assert 'Yeni Post' in response.data.decode('utf-8')


def test_health_check():
    tester = app.test_client()
    response = tester.get('/health')
    assert response.status_code == 200
    assert response.data == b'OK'
