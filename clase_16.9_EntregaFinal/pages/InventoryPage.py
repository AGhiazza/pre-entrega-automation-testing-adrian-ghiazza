from selenium.webdriver.common.by import By 


class InventoryPage:
    def __init__(self, driver):
    
        self.driver = driver

        #Selectores
        self.item_list = (By.CLASS_NAME, "inventory_item")
        self.add_to_cart = (By.CLASS_NAME, "btn_inventory")
        self.go_to_cart = (By.CLASS_NAME, "shopping_cart_link")
        
    def agregar_al_carrito(self, numProd): #Función para agregar un producto al carrito, numProd recibe el numero del indice para elegir cual producto agregar.
        productos = self.driver.find_elements(*self.item_list)
        producto = productos [numProd] #de la lista de productos guarda el producto segun el indice recibido
        producto.find_element(*self.add_to_cart).click()
      

    def ir_al_carrito(self): #función para clickear en el botón de ir al carrito
        self.driver.find_element(*self.go_to_cart).click() #busca el botón para ir al carrito

