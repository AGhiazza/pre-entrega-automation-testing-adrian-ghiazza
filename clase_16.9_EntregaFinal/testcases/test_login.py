from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def test_LO01_login_exitoso(login_in_driver):
    driver = login_in_driver
    WebDriverWait (driver, 5).until(
        EC.url_contains("/inventory.html")
    )
    assert "/inventory.html" in driver.current_url, "No se visualiza la pagina del inventario"

'''
def test_LO02_():
def test_LO03_():
def test_LO04_():
def test_LO05_():
'''