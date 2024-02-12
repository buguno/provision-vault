from http import HTTPStatus


def test_should_return_200_and_hello_prepper_message(client):
    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Hello, prepper!'}


def test_should_return_new_user_created_and_status_code_201(client):
    response = client.post(
        '/users/',
        json={
            'username': 'reece',
            'password': 'secret',
        },
    )

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'id': 1,
        'username': 'reece',
    }


def test_should_return_all_users(client):
    response = client.get('/users/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [
            {
                'id': 1,
                'username': 'reece',
            }
        ]
    }
