import pytest
from fastapi.testclient import TestClient

from madrs.app import app


@pytest.fixture
def client():
    return TestClient(app)
