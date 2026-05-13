from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys 


def login(driver):  #se llama al driver fixture del conftest
    driver.get("https://www.saucedemo.com/")

    #Usuario
    usuario = driver.find_element(By.ID, "user-name")   
    usuario.send_keys("standard_user")      

    #Pass
    contrasena = driver.find_element(By.ID, "password") 
    contrasena.send_keys("secret_sauce")

    #Submit
    contrasena.send_keys(Keys.RETURN) 

