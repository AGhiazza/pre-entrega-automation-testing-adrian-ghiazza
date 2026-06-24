import pytest
from selenium import webdriver
from pages.LoginPage import LoginPage
from utils.data_reader import read_users_csv
import pathlib
from pytest_html import extras
from datetime import datetime
from pytest_metadata.plugin import metadata_key

# Crear carpetas de reportes automáticamente
pathlib.Path("reports").mkdir(exist_ok=True)
pathlib.Path("reports/logs").mkdir(exist_ok=True)

@pytest.fixture
def driver(): # Fixture que abre Chrome con las opciones configuradas y lo cierra al terminar el test
    options = webdriver.ChromeOptions() 
    options.add_argument("--incognito") # Modo incógnito para evitar caché y cookies de sesiones anteriores
    options.add_argument("--headless=new") # Modo sin interfaz visual
    options.add_argument("--no-sandbox") # Requerido para correr en entornos Linux/CI
    options.add_argument("--disable-dev-shm-usage") # Evita errores de memoria compartida en Linux
    options.add_argument("--window-size=1920,1080") # Define resolución para evitar problemas de elementos fuera de pantalla
    options.add_argument("--disable-gpu") # Desactiva GPU, recomendado en modo headless

    driver = webdriver.Chrome(options=options) 

    yield driver # Punto de ejecución del test — todo lo anterior es setup, todo lo posterior es teardown

    driver.quit() # Cierra el navegador al finalizar el test

@pytest.fixture #Este fixture recibe el driver y llama a la funcion de login de LoginPage.py, devuelve el driver ya logueado
def driver_logged(driver):
    login_page = LoginPage(driver)
    users = read_users_csv()
    for user in users:  #For para buscar un registro en el CSV cuyo valor para "valido" sea "True"
        if user["valido"] == "true":
            break
    login_page.login_completo(user["usuario"], user["contrasena"])
    return(driver)

@pytest.hookimpl(tryfirst=True, hookwrapper=True) 
def pytest_runtest_makereport(item, call): 

    outcome = yield     #pausa el hook y espera que el test corra, guardando el resultado en outcome

    report = outcome.get_result()   

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver") 

        if driver: #Si driver=true, el test es de UI, si es de API va a estar en "None"
            target = pathlib.Path("reports/screenshots") #guarda la dirección donde se guardará el reporte
            target.mkdir(parents=True, exist_ok=True) #crea la carpeta

            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

            file_name = target / f"{item.name}_{timestamp}.png" #Guarda la ruta entera "reports/screenshots/test_CA01_cart_badge.png" item.name trae el "name" del test
            
            driver.save_screenshot(str(file_name)) 

            extra = getattr(report, "extras", []) #Obtiene lista de extras que ya tenga el reporte
            extra.append(extras.png(f"screenshots/{item.name}_{timestamp}.png")) #agrega la captura a la lista
            report.extras = extra #guarda la lista actualizada de vuelta en el reporte HTML

#Configuraciones del reporte HTML
def pytest_html_report_title(report):
    report.title = "TT26143 - Automation Framework - Saucedemo"

def pytest_configure(config):
    config.stash[metadata_key]["Proyecto"] = "TT26143 - Automation Framework - Saucedemo"
    config.stash[metadata_key]["Autor"] = "Adrian Ghiazza"
    config.stash[metadata_key]["Comisión"] = "26143"