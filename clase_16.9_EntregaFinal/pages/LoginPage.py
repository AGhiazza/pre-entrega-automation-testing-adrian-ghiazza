from selenium.webdriver.common.by import By 


class LoginPage:     #define la clase que representa la pagina del login
    def __init__(self, driver):     #Constructor: Funcion/metodo que ejectura todo su código automaticamente cuando se crea un objeto de esta clase.
                                    #Self refiere al objeto mismo que se crea con esta clase
        self.driver = driver #Se va a guardar el navegador dentro de la clase.
        
        # Selectores
        self.username_input = (By.ID, "user-name")
        self.password_input = (By.ID, "password")
        self.login_button = (By.ID, "login-button")
        self.error_message = (By.CSS_SELECTOR, "[data-test='error']")
        
    def abrir_pagina(self): #funcion que abre el navegador
        self.driver.get("https://www.saucedemo.com/") # .get de selenium para abrir la pagina web

    def ingresar_usuario(self, usuario): #función que ingresa el usuario
        self.driver.find_element(*self.username_input).send_keys(usuario) # En vez de hardcodear el selector, lo llama desde la clase LoginPage
                                                       # el asterisco * desempaqueta la información de la variable que le sigue, es decir busca la variable, accede a su contenido y lo "extrae"

    def ingresar_contrasena(self, contrasena): #función que ingresa contraseña
        self.driver.find_element(*self.password_input).send_keys(contrasena)

    def click_login(self): #función que hace click en login
        self.driver.find_element(*self.login_button).click()
    
    def login_completo(self, usuario, contrasena):  #función para hacer login completo
        self.abrir_pagina()
        self.ingresar_usuario(usuario)
        self.ingresar_contrasena(contrasena)
        self.click_login()

    def mensaje_error(self):
        return self.driver.find_element(*self.error_message).text

