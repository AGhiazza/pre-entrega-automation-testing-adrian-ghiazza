import pytest
from selenium.webdriver.support.ui import WebDriverWait 
from pages.LoginPage import LoginPage 
from selenium.webdriver.support import expected_conditions as EC
from utils.logger import logger
from utils.config import INVENTORY_PATH

@pytest.mark.ui
def test_LO01_login_exitoso(driver):
    logger.info("=== Iniciando test_LO01_login_exitoso ===")
    login_page = LoginPage(driver)

    login_page.login_completo("standard_user","secret_sauce")
    WebDriverWait (driver, 5).until( #espera hasta 5 segundos o hasta que se cumpla la condicion definida abajo
        EC.url_contains(INVENTORY_PATH)  #se indica que la condición esperada para la espera explicita es que la URL contenga "/inventory.html"
    )
    assert INVENTORY_PATH in driver.current_url, "No se visualiza la pagina del inventario" 

@pytest.mark.ui
def test_LO02_login_fallido_campos_vacios(driver):
    logger.info("=== Iniciando test_LO02_login_fallido_campos_vacios ===")
    login_page = LoginPage(driver)
    logger.info(f"Abriendo pagina web{driver.current_url}")
    login_page.abrir_pagina()
    logger.info("Intentando login")
    login_page.click_login()
    logger.info("Verificando mensaje de error")
    mensaje_error = login_page.obtener_mensaje_error()
    assert "Epic sadface" in mensaje_error, "No se visualiza el mensaje de error correcto"