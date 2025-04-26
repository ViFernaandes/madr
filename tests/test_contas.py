from http import HTTPStatus


def test_deve_cadastrar_uma_conta(client):
    response = client.post(
        '/conta/',
        json={'username': 'test', 'email': 'user@test.com', 'password': '123'},
    )
    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'username': 'test',
        'email': 'user@test.com',
        'id': 1,
    }


def test_deve_retornar_todas_contas(client):
    response = client.get('/conta/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'contas': [
            {
                'username': 'test',
                'email': 'user@test.com',
                'id': 1,
            },
        ]
    }


def test_deve_alterar_uma_conta_cadastrada(client):
    response = client.put(
        '/conta/1',
        json={'username': 'test', 'email': 'user@test.com', 'password': '123'},
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'id': 2,
        'username': 'test',
        'email': 'user@test.com',
    }


def test_deve_excluir_uma_conta(client):
    response = client.delete(
        '/conta/1',
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Conta Deleted'}
