import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from app import app

def test_index():
    tester = app.test_client()
    response = tester.get('/')
    assert response.status_code == 200
    assert b'Hen\xfcz yaz\xc4\xb1 yok' in response.data  # "Henüz yazı yok" mesajını kontrol et


