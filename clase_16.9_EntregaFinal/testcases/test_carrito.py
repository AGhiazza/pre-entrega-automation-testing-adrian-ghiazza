from selenium.webdriver.common.by import By
from funcAux.InventoryPage import agregar_al_carrito, ir_al_carrito

def test_CA01_cart_badge(driver_logged):    #Caso para verificar que se muestre el numero de productos cuando se agrega al menos 1 al carrito
    agregar_al_carrito(driver_logged, 0)    #llama a la función agregar_al_carrito y le dá el indice 0 para decirle que busque el primer producto
    carritoBadge = driver_logged.find_element(By.CLASS_NAME, "shopping_cart_badge") #busca el elemento de la marca de cantidad de prodcutos en el carrito y lo guarda en la variable
    assert carritoBadge.is_displayed(), "No se visualiza badge del carrito"

def test_CA02_cart_badge_increase(driver_logged):   #Caso para agregar 2 productos al carrito y ver que el contador suba.
    agregar_al_carrito(driver_logged, 0)
    agregar_al_carrito(driver_logged, 1)
    carritoBadge = driver_logged.find_element(By.CLASS_NAME, "shopping_cart_badge")
    carritoBadgeNum = int(carritoBadge.text)    #Toma el texto en la variable del contador del carrito y lo convierte en integer para despues comparar
    print(f"Cantidad de Productos en el carrito: {carritoBadgeNum}")    #Imprime por consola la cantidad de productos agregados
    assert carritoBadgeNum == 2, "No se visualiza la cantidad correcta de productos en el icono del carrito"    #valida que la cantidad de prodcutos sea igual a 2

def test_CA03_go_to_cart(driver_logged):    #Caso para validar que cuando se navega al carrito se visualice la pagina correcta.
    ir_al_carrito(driver_logged)
    assert "/cart.html" in driver_logged.current_url, "No se visualiza la pagina del carrito"   

def test_CA04_check_item_in_cart(driver_logged):    #Caso para validar que las caracteristicas de un producto sean iguales en el inventario como en el carrito
    productos = driver_logged.find_elements(By.CLASS_NAME, "inventory_item")
    primerProducto = productos [0]
    nombreInv = str(primerProducto.find_element(By.CLASS_NAME, "inventory_item_name").text) #Guarda el nombre del producto en el inventario.
    precioInv = str(primerProducto.find_element(By.CLASS_NAME, "inventory_item_price").text) #Guarda el precio del producto en el inventario.
    descrpInv = str(primerProducto.find_element(By.CLASS_NAME, "inventory_item_desc").text) #Guarda la descripción del producto en el inventario.
    agregar_al_carrito(driver_logged, 0)
    ir_al_carrito(driver_logged)
    productoEnCarrito = driver_logged.find_element(By.CLASS_NAME, "cart_item")  #Busca la tarjeta del producto dentro del carrito.
    nombreCar = str(productoEnCarrito.find_element(By.CLASS_NAME, "inventory_item_name").text)  #Guarda el nombre del producto en el carrito.
    precioCar = str(productoEnCarrito.find_element(By.CLASS_NAME, "inventory_item_price").text)
    descrpCar = str(productoEnCarrito.find_element(By.CLASS_NAME, "inventory_item_desc").text)
    assert nombreInv == nombreCar, "El nombre del producto en el catálogo difiere al del carrito"   #Compara los nombres del producto fuera en el invetorio contra los del carrito
    assert precioInv == precioCar, "El precio del producto en el catálogo difiere al del carrito"
    assert descrpInv == descrpCar, "La descripción del producto en el catálogo difiere a la del carrito"
