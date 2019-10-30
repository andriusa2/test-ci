import pytest
from app.main import app as my_app


@pytest.yield_fixture
def app():
    yield my_app


@pytest.fixture
def test_cli(loop, app, sanic_client):
    return loop.run_until_complete(sanic_client(app))

