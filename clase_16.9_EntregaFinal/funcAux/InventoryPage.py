from selenium.webdriver.common.by import By 

def agregar_al_carrito(driver, numProd): #Función para agregar un producto al carrito, numProd recibe el numero del indice para elegir cual producto agregar.
    productos = driver.find_elements(By.CLASS_NAME, "inventory_item") #guarda todos los productos como lista usando find_elements en "productos"
    producto = productos [numProd] #de la lista de productos guarda el producto segun el indice recibido
    anadirCarrito = producto.find_element(By.CLASS_NAME, "btn_inventory")
    anadirCarrito.click()

def ir_al_carrito(driver):
    botonCarrito = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
    botonCarrito.click()