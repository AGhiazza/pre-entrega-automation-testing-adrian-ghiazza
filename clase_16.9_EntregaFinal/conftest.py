import pytest
from selenium import webdriver #importa el modulo webdriver que controla el navegador para hacer las pruebas
from funcAux.LoginPage import login #Importa el login desde la carpeta de funciones auxiliares -> LoginPage.py


@pytest.fixture #el .fixture es una función reutilizable que varios test pueden usar como parametro.
                #pytest lo gestiona cuando un test lo necesita
def driver(): 
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")

    driver = webdriver.Chrome(options=options)

    yield driver #marca la ejecución de la prueba, todo el código anterior (↑) se ejecuta antes que la prueba arranque
                 #y todo lo posterior (↓) se ejecuta luego de finalizar la prueba

    driver.quit() #Cierra el navegador

@pytest.fixture #Este fixture recibe el driver y llama a la funcion de login de LoginPage.py, devuelve el driver ya logueado
def driver_logged(driver):
    login(driver)
    return(driver)