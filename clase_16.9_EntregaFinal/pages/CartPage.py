from selenium.webdriver.common.by import By

class CartPage:
    def __init__(self, driver):
        
        self.driver = driver

        #Selectores
        self.app_logo = (By.CLASS_NAME, "app_logo")
        self.your_cart_title = (By.CLASS_NAME, "title")

        self.cart_list = (By.CLASS_NAME, "cart_list")
        self.cart_item_container = (By.CLASS_NAME, "cart_item") #Listado de productos
        self.cart_item_qty = (By.CLASS_NAME, "cart_quantity")

        self.cart_item_details = (By.CLASS_NAME, "cart_item_label") #contenedor de de 1 producto
        self.cart_item_name = (By.CLASS_NAME, "inventory_item_name")
        self.cart_item_desc = (By.CLASS_NAME, "inventory_item_desc")
        self.cart_item_price = (By.CLASS_NAME, "inventory_item_price")

        self.remove_button = (By.CSS_SELECTOR, "[data-test^='remove']") #El ^= significa "que empiece con", así agarra cualquier botón remove sin importar el producto.

        self.continue_shopping = (By.ID, "continue-shopping")
        self.checkout = (By.ID, "checkout")

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
        self.driver.find_element(*self.continue_shopping).click()

    def ir_a_checkout(self):
        self.driver.find_element(*self.checkout).click()

