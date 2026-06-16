import requests
import pytest
from utils.api_utils import BASE_URL, HEADERS
from utils.logger import logger

@pytest.mark.api
def test_APIUS01_obtener_usuario():
    logger.info("=== Iniciando test_APIUS01_obtener_usuario ===")
    response = requests.get(BASE_URL+"/api/users/2", headers=HEADERS)

    assert response.status_code == 200
    print (response.elapsed.total_seconds())
    assert response.elapsed.total_seconds() < 2 #menos de dos segundos

@pytest.mark.api
def test_APIUS02_crear_usuario():
    logger.info("=== Iniciando test_APIUS02_crear_usuario ===")
    body = {
        "name": "juancho",
        "email": "aghiazzabna@gmail.com",
        "password": "12345",
    }

    response = requests.post(BASE_URL+"/api/users", headers=HEADERS, json=body)

    data = response.json()

    assert response.status_code == 201, "No se pudo crear el usuario."
    assert data["name"] == body["name"], "El nombre no se generó correctamente."
    assert data["email"] == body["email"], "El email no se generó correctamente."
    assert data["password"] == body["password"], "La contraseña no se generó correctamente."

@pytest.mark.api
def test_APIUS03_eliminar_usuario():
    logger.info("=== Iniciando test_APIUS03_eliminar_usuario ===")
    response = requests.delete(BASE_URL+"/api/users/2", headers=HEADERS)

    assert response.status_code == 204