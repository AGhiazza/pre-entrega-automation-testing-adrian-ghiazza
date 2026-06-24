from selenium.webdriver.common.by import By 
from utils.config import BASE_URL_UI

class LoginPage:     
    def __init__(self, driver):     
        self.driver = driver
        
        # Selectores
        self.username_input = (By.ID, "user-name")
        self.password_input = (By.ID, "password")
        self.login_button = (By.ID, "login-button")
        self.error_message = (By.CSS_SELECTOR, "[data-test='error']")   #Mensaje de error al fallar el ingreso
        
    def abrir_pagina(self): #Método que abre el navegador
        self.driver.get(BASE_URL_UI) # .get de selenium para abrir la pagina web

    def ingresar_usuario(self, usuario): 
        self.driver.find_element(*self.username_input).send_keys(usuario) 

    def ingresar_contrasena(self, contrasena): 
        self.driver.find_element(*self.password_input).send_keys(contrasena)

    def click_login(self): 
        self.driver.find_element(*self.login_button).click()
    
    def login_completo(self, usuario, contrasena):  #Método para hacer login completo
        self.abrir_pagina()
        self.ingresar_usuario(usuario)
        self.ingresar_contrasena(contrasena)
        self.click_login()

    def obtener_mensaje_error(self):
        return self.driver.find_element(*self.error_message).text

