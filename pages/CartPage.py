from selenium.webdriver.common.by import By
from pages.BasePage import BasePage

class CartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver) #Importa los atributos y métodos de BasePage

        #Selectores
        
        self.your_cart_title = (By.CLASS_NAME, "title") # Texto "Your Cart"

        self.cart_list = (By.CLASS_NAME, "cart_list")   # Contenedor de Carrito entero (con "titulos" de QTY y Description)
        
        self.cart_item_container = (By.CLASS_NAME, "cart_item") #Contenedor de cart_quantity y cart_item_label (Tarjeta con Cantidad de productos + Detalles del producto)
        self.cart_item_qty = (By.CLASS_NAME, "cart_quantity")   #Cantidad de items en el carrito de un producto especifico 


        self.cart_item_details = (By.CLASS_NAME, "cart_item_label") #contenedor de Titulo, Desc, precio y remove de 1 producto
        self.cart_item_name = (By.CLASS_NAME, "inventory_item_name")
        self.cart_item_desc = (By.CLASS_NAME, "inventory_item_desc")
        self.cart_item_price = (By.CLASS_NAME, "inventory_item_price")

        self.remove_button = (By.CSS_SELECTOR, "[data-test^='remove']") #Botón de Remove del carrito.

        self.continue_shopping_button = (By.ID, "continue-shopping")
        self.checkout_button = (By.ID, "checkout")

    # Métodos para productos

    def obtener_productos(self):
        return self.driver.find_elements(*self.cart_item_container)
        
    def obtener_nombre_producto(self, numProd):
        productos = self.driver.find_elements(*self.cart_item_container)
        producto = productos[numProd]
        return producto.find_element(*self.cart_item_name).text

    def obtener_descripcion_producto(self, numProd):
        productos = self.driver.find_elements(*self.cart_item_container)
        producto = productos[numProd]
        return producto.find_element(*self.cart_item_desc).text

    def obtener_precio_producto(self, numProd):
        productos = self.driver.find_elements(*self.cart_item_container)
        producto = productos[numProd]
        return producto.find_element(*self.cart_item_price).text

    # Métodos para carrito

    def remover_del_carrito(self,numProd):
        productos = self.driver.find_elements(*self.cart_item_container)
        producto = productos [numProd]
        producto.find_element(*self.remove_button).click()

    def continuar_comprando(self):
        self.driver.find_element(*self.continue_shopping_button).click()

    def ir_a_checkout(self):
        self.driver.find_element(*self.checkout_button).click()

