from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_registration_with_correct_creds():
    response = client.post(
        "/auth/register",
        json={"name": "admin", "email": "admin@example.com", "password": "12345678"},
    )
    assert response.status_code == 200
    assert response.json() == {"name": "admin", "email": "admin@example.com"}


def test_registration_with_incorrect_email():
    response = client.post(
        "/auth/register",
        json={"name": "olga", "email": "151ignsocrrect0mail", "password": "12345678"},
    )
    assert response.status_code == 422
    assert response.json() == {"detail": "Incorrect email value"}


def test_registration_with_incorrect_password():
    response = client.post(
        "/auth/register",
        json={"name": "olga", "email": "olga@mail.ru", "password": "666"},
    )
    assert response.status_code == 422
    assert response.json() == {
        "detail": "Incorrect password (must contain minimum 8 symbols)"
    }


def test_login_with_correct_creds():
    response = client.post(
        "/auth/login", data={"username": "admin", "password": "12345678"}
    )
    assert response.status_code == 200
    assert response.json().get("user_name") == "admin"


def test_login_with_inorrect_user():
    response = client.post(
        "/auth/login", data={"username": "adminatutnet", "password": "amnot a password"}
    )
    assert response.status_code == 401
    assert response.json() == {"detail": "Invalid login"}


def test_login_with_inorrect_password():
    response = client.post(
        "/auth/login", data={"username": "admin", "password": "amnot a password"}
    )
    assert response.status_code == 401
    assert response.json() == {"detail": "Incorrect password"}
