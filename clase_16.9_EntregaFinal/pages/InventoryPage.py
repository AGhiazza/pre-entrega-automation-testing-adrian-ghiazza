from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import Select

class InventoryPage:
    def __init__(self, driver):
    
        self.driver = driver

        #Selectores
        self.app_logo = (By.CLASS_NAME, "app_logo")
        self.item_list = (By.CLASS_NAME, "inventory_list") 
        self.item_details = (By.CLASS_NAME, "inventory_item")
        self.item_name = (By.CLASS_NAME, "inventory_item_name")
        self.item_desc = (By.CLASS_NAME, "inventory_item_desc")
        self.item_price = (By.CLASS_NAME, "inventory_item_price")
        self.item_img = (By.CLASS_NAME, "inventory_item_img")
        self.add_to_cart = (By.CLASS_NAME, "btn_inventory")
        self.go_to_cart = (By.CLASS_NAME, "shopping_cart_link")
        self.cart_badge = (By.CLASS_NAME, "shopping_cart_badge")
        self.burguer = (By.ID, "react-burger-menu-btn") 
        self.allitems_button = (By.ID, "inventory_sidebar_link")
        self.about = (By.ID, "about_sidebar_link")
        self.logout = (By.ID, "logout_sidebar_link")
        self.resetapp = (By.ID, "reset_sidebar_link")
        self.close_burguer = (By.ID, "react-burger-cross-btn")
        self.sort = (By.CLASS_NAME, "product_sort_container")  #Boton de ordenamiento es un <select> de HTML


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

    # Métodos ícono ordenar (sort)

    def obtener_ordenar(self):
        return self.driver.find_element(*self.sort)

    def ordenar(self, criterio):
        # Valores disponibles: "az" (A-Z), "za" (Z-A), "lohi" (precio menor a mayor), "hilo" (precio mayor a menor)
        botonOrdenar = self.driver.find_element(*self.sort)
        Select(botonOrdenar).select_by_value(criterio)

    # Métodos para productos

    def obtener_productos(self):
        return self.driver.find_elements(*self.item_details)
        
    def obtener_nombre_producto(self, numProd):
        productos = self.driver.find_elements(*self.item_details)
        producto = productos[numProd]
        return producto.find_element(*self.item_name).text

    def obtener_precio_producto(self, numProd):
        productos = self.driver.find_elements(*self.item_details)
        producto = productos[numProd]
        return producto.find_element(*self.item_price).text

    def agregar_al_carrito(self, numProd): #Función para agregar un producto al carrito, numProd recibe el numero del indice para elegir cual producto agregar.
        productos = self.driver.find_elements(*self.item_details)
        producto = productos [numProd] #de la lista de productos guarda el producto segun el indice recibido
        producto.find_element(*self.add_to_cart).click()

    # Métodos para carrito

    def obtener_carrito(self):
        return self.driver.find_element(*self.go_to_cart)

    def obtener_cantidad_carrito(self):
        return self.driver.find_element(*self.cart_badge).text
    
    def ir_al_carrito(self): #función para clickear en el botón de ir al carrito
        self.driver.find_element(*self.go_to_cart).click() #busca el botón para ir al carrito
