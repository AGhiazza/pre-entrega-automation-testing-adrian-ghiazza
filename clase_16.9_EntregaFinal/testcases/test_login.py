from selenium.webdriver.support.ui import WebDriverWait #WebDriverWait hace esperas explicitas, el sistema espera un tiempo definido hasta que ocurra una cierta condición, 
                                                        #si la condicion se cumple antes de que pase el tiempo definido, avanza ignorando el tiempo restante
from pages.LoginPage import LoginPage #Importa la clase LoginPage desde LoginPage.py adentro de la carpeta pages
from selenium.webdriver.support import expected_conditions as EC #expected_conditions es un módulo que tiene condiciones predefinidas para usar con WebDriverWait. Por ejemplo "esperá hasta que pase X"
                                                                 #Se usa el "as EC" para acortar expected_conditions, escribir EC = Expected_conditions

def test_LO01_login_exitoso(driver):
    login_page = LoginPage(driver) # El objeto login_page almacena la clase LoginPage con el driver
    login_page.login_completo("standard_user","secret_sauce")
    WebDriverWait (driver, 5).until( #espera hasta 5 segundos o hasta que se cumpla la condicion definida abajo
        EC.url_contains("/inventory.html")  #se indica que la condición esperada para la espera explicita es que la URL contenga "/inventory.html"
                                            #El sistema espera entonces que aparezca "/inventory.html" en la URL o que pasen 5 segundos antes de avanzar
    )
    assert "/inventory.html" in driver.current_url, "No se visualiza la pagina del inventario" #verifica que la URL actual incluya "/inventory.html". 
                                                                                               #Si no, el test falla con el mensaje de error "No se visualiza la pagina del inventario".

def test_LO02_login_fallido_campos_vacios(driver):
    login_page = LoginPage(driver)
    login_page.abrir_pagina()
    login_page.click_login()
    mensaje_error = login_page.mensaje_error()
    assert "Username is required" in mensaje_error, "No se visualiza el mensaje de error correcto"