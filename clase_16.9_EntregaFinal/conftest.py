import pytest
from selenium import webdriver #importa el modulo webdriver que controla el navegador para hacer las pruebas
from pages.LoginPage import LoginPage

@pytest.fixture #el .fixture es un decorador o etiqueta quie marca esta función como reutilizable para que varios test la pueden usar como parametro
def driver(): 
    options = webdriver.ChromeOptions() #Crea la variable "options" y guarda la configuración de chrome
    options.add_argument("--incognito") #Agrega argumento incognito a las opciones de Chrome, en este caso, los argumentos son parametros para modificar el comportamiento del navegador

    driver = webdriver.Chrome(options=options) #abre chrome con las opciones configuradas que se guardaron antes y se guarda todo en la variable driver.
                                               #la variable driver es la que usan los tests para interactuar con el navegador.

    yield driver #marca la ejecución de la prueba, todo el código anterior (↑) se ejecuta antes que la prueba arranque
                 #y todo lo posterior (↓) se ejecuta luego de finalizar la prueba

    driver.quit() #Cierra el navegador

@pytest.fixture #Este fixture recibe el driver y llama a la funcion de login de LoginPage.py, devuelve el driver ya logueado
def driver_logged(driver):
    login_page = LoginPage(driver)
    login_page.login_completo("standard_user","secret_sauce")
    return(driver)