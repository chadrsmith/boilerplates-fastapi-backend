import pytest
from fastapi.testclient import TestClient
from app.main import init_app

@pytest.fixture('session')
def test_app_client():
    client = TestClient(init_app())
    ### Set client attributes ###
    return client