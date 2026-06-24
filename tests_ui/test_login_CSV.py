from selenium.webdriver.support.ui import WebDriverWait 
from pages.LoginPage import LoginPage 
from selenium.webdriver.support import expected_conditions as EC 
from utils.data_reader import read_users_csv

import pytest
from utils.logger import logger
from utils.config import INVENTORY_PATH

@pytest.mark.ui
@pytest.mark.parametrize("user", read_users_csv(), ids=[elemento["descripcion"] for elemento in read_users_csv()]) #Usa el valor de la columna "descripcion" del archivo CSV como ID del caso en los resultados.
def test_LO01_login(driver, user):
    logger.info(f"=== Iniciando test_LO01_login con usuario -{user['usuario']}- ===")
    login_page = LoginPage(driver)
    logger.info(f"Intentando login con usuario: {user['usuario']}")
    login_page.login_completo(user["usuario"], user["contrasena"])
    if user["valido"] == "true": #Si el user está marcado como "Valido" en el CSV se espera que ingrese correctamente, sino que falle (va al else)
        WebDriverWait (driver, 5).until( 
            EC.url_contains(INVENTORY_PATH)
        )
        assert INVENTORY_PATH in driver.current_url, "No se visualiza la pagina del inventario" 
        logger.info("Login exitoso - redirigido a inventario")
    else:
        logger.info("Login fallido - verificando mensaje de error")
        error = login_page.obtener_mensaje_error()
        assert "Epic sadface" in error