import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from app import app

def test_index():
    tester = app.test_client()
    response = tester.get('/')
    assert response.status_code == 200
    html = response.data.decode('utf-8')
    assert 'Henüz yazı yok' in html  # daha güvenilir ve okunabilir



