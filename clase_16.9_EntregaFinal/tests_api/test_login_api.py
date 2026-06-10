import requests
from utils.api_utils import BASE_URL, HEADERS
import pytest
from utils.data_reader import read_json_files


@pytest.mark.parametrize("user", read_json_files("login_cases.json"), ids=[elemento["descripcion"] for elemento in read_json_files("login_cases.json")])
def test_APILO01_login(user):
    
    response = requests.post(BASE_URL+"/api/login", headers=HEADERS, json=user)

    if user["valido"] == "true":
        assert response.status_code == 200, "El login falló"
    else:
        assert response.status_code == 400, "Se devolvió Status Code distinto de 400"