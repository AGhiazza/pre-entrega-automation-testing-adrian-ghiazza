from selenium.webdriver.support.ui import WebDriverWait #WebDriverWait hace esperas explicitas, el sistema espera un tiempo definido hasta que ocurra una cierta condición, 
                                                        #si la condicion se cumple antes de que pase el tiempo definido, avanza ignorando el tiempo restante
from pages.LoginPage import LoginPage #Importa la clase LoginPage desde LoginPage.py adentro de la carpeta pages
from selenium.webdriver.support import expected_conditions as EC #expected_conditions es un módulo que tiene condiciones predefinidas para usar con WebDriverWait. Por ejemplo "esperá hasta que pase X"
                                                                 #Se usa el "as EC" para acortar expected_conditions, escribir EC = Expected_conditions
from utils.data_reader import read_users_csv

import pytest
from utils.logger import logger


@pytest.mark.ui
@pytest.mark.parametrize("user", read_users_csv(), ids=[elemento["descripcion"] for elemento in read_users_csv()]) #Usa el valor de la columna "descripcion" del archivo CSV como ID del caso en los resultados.
def test_LO01_login(driver, user):
    logger.info(f"=== Iniciando test_LO01_login con usuario -{user['usuario']}- ===")
    login_page = LoginPage(driver)
    logger.info(f"Intentando login con usuario: {user['usuario']}")
    login_page.login_completo(user["usuario"], user["contrasena"])
    if user["valido"] == "true":
        WebDriverWait (driver, 5).until( #espera hasta 5 segundos o hasta que se cumpla la condicion definida abajo
            EC.url_contains("/inventory.html")  #se indica que la condición esperada para la espera explicita es que la URL contenga "/inventory.html"
                                            #El sistema espera entonces que aparezca "/inventory.html" en la URL o que pasen 5 segundos antes de avanzar
        )
        assert "/inventory.html" in driver.current_url, "No se visualiza la pagina del inventario" #verifica que la URL actual incluya "/inventory.html". 
        logger.info("Login exitoso - redirigido a inventario")
    else:
        logger.info("Login fallido - verificando mensaje de error")
        error = login_page.mensaje_error()
        assert "Epic sadface" in error