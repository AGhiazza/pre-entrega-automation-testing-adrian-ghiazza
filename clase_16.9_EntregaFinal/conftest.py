import pytest
from selenium import webdriver #importa el modulo webdriver que controla el navegador para hacer las pruebas
from pages.LoginPage import LoginPage
from utils.data_reader import read_users_csv
import pathlib
from pytest_html import extras
from datetime import datetime

# Crear carpetas de reportes automáticamente
pathlib.Path("reports").mkdir(exist_ok=True)
pathlib.Path("logs").mkdir(exist_ok=True)

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
    users = read_users_csv()
    for user in users:  #For para buscar un registro cuyo valor para "valido" sea "T"rue"
        if user["valido"] == "true":
            break
    login_page.login_completo(user["usuario"], user["contrasena"])
    return(driver)

@pytest.hookimpl(tryfirst=True, hookwrapper=True) # tryfirst hace que corra este hook antes que el resto, wrapper hace que pause este hook (que normalmente se ejecuta solo antes) espere hasta que termine el test
def pytest_runtest_makereport(item, call): #Funcion reservada de Pytest, se ejecuta 3 veces (setup, call, teardown) generando un reporte en cada oportunidad
                                          #item es el test como objeto con su metadata y el call es esta instancia puntual de prueba
    outcome = yield     #pausa el hook y espera que el test corra, guardando el resultado en outcome

    report = outcome.get_result()   #get_result es un método que desenvuelve el contenido guardado en outcome con atributos como "report.when" "report.passed" y "report.failed"

    # when puede ser = a setup (preparación), call(ejecución) o teardown(finalización)
    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver") #item.funcargs es un diccionario que contiene todos los fixtures del test que se está ejecutando

        if driver: #Si driver=true, el test es de UI, si es de API va a estar en "None"
            target = pathlib.Path("reports/screenshots") #guarda la dirección donde se guardará el reporte
            target.mkdir(parents=True, exist_ok=True) #crea la carpeta, "parents=true" si la carpeta padre /reports no existe la crea, exist_ok=true evita que falle si la carpeta ya existe

            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

            file_name = target / f"{item.name}_{timestamp}.png" #Guarda la ruta entera "reports/screenshots/test_CA01_cart_badge.png" item.name trae el "name" del test
            
            driver.save_screenshot(str(file_name)) #Guarda la screenshot

            extra = getattr(report, "extras", []) #Obtiene lista de extras que ya tenga el reporte
            extra.append(extras.png(str(file_name))) #agrega la captura a la lista
            report.extras = extra #guarda la lista actualizada de vuelta en el reporte HTML