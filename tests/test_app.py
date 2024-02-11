from http import HTTPStatus

from fastapi.testclient import TestClient

from app.app import app


def test_should_return_200_and_hello_prepper_message():
    client = TestClient(app)

    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Hello, prepper!'}
