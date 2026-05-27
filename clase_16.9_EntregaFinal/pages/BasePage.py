from selenium.webdriver.common.by import By

class BasePage:
    def __init__(self, driver):
        
        self.driver = driver

        #Selectores
        self.app_logo = (By.CLASS_NAME, "app_logo")
        self.go_to_cart = (By.CLASS_NAME, "shopping_cart_link")
        self.cart_badge = (By.CLASS_NAME, "shopping_cart_badge")
        self.burguer = (By.ID, "react-burger-menu-btn") 
        self.allitems_button = (By.ID, "inventory_sidebar_link")
        self.about = (By.ID, "about_sidebar_link")
        self.logout = (By.ID, "logout_sidebar_link")
        self.resetapp = (By.ID, "reset_sidebar_link")
        self.close_burguer = (By.ID, "react-burger-cross-btn")

    def obtener_titulo(self):
        return self.driver.find_element(*self.app_logo).text
    
    # Métodos menú hamburguesa

    def obtener_hamburguesa(self):
        return self.driver.find_element(*self.burguer)

    def abrir_hamburguesa(self):
        self.driver.find_element(*self.burguer).click()

    def click_allitems(self):
        self.driver.find_element(*self.allitems_button).click()

    def click_about(self):
        self.driver.find_element(*self.about).click()

    def click_logout(self):
        self.driver.find_element(*self.logout).click()

    def click_reset_app(self):
        self.driver.find_element(*self.resetapp).click()

    def cerrar_hamburguesa(self):
        self.driver.find_element(*self.close_burguer).click()

    # Métodos para carrito

    def obtener_carrito(self):
        return self.driver.find_element(*self.go_to_cart)

    def obtener_cantidad_carrito(self):
        return self.driver.find_element(*self.cart_badge).text
    
    def ir_al_carrito(self): #función para clickear en el botón de ir al carrito
        self.driver.find_element(*self.go_to_cart).click() #busca el botón para ir al carrito
