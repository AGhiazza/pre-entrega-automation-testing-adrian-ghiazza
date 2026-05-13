import pytest
from selenium import webdriver
from funcAux.LoginPage import login #Importa el login desde utils->LoginPage.py


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")

    driver = webdriver.Chrome(options=options)

    yield driver

    driver.quit()

@pytest.fixture
def login_in_driver(driver):
    login(driver)
    return(driver)

@pytest.fixture

def driver_logged(login_in_driver):
    driver = login_in_driver
    return driver