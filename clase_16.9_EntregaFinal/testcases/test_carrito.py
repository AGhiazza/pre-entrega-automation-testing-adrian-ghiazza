from selenium.webdriver.common.by import By
from funcAux.InventoryPage import agregar_al_carrito, ir_al_carrito

def test_CA01_cart_badge(driver_logged):
    agregar_al_carrito(driver_logged, 0) #llama a la función agregar_al_carrito y le dá el indice 0 para decirle que busque el primer producto
    carritoBadge = driver_logged.find_element(By.CLASS_NAME, "shopping_cart_badge")
    assert carritoBadge.is_displayed(), "No se visualiza badge del carrito"

def test_CA02_cart_badge_increase(driver_logged):
    agregar_al_carrito(driver_logged, 0)
    agregar_al_carrito(driver_logged, 1)
    carritoBadge = driver_logged.find_element(By.CLASS_NAME, "shopping_cart_badge")
    carritoBadgeNum = int(carritoBadge.text)
    print(f"Cantidad de Productos en el carrito: {carritoBadgeNum}")
    assert carritoBadgeNum == 2, "No se visualiza la cantidad correcta de productos en el icono del carrito"

def test_CA03_go_to_cart(driver_logged):
    ir_al_carrito(driver_logged)
    assert "/cart.html" in driver_logged.current_url, "No se visualiza la pagina del carrito"

def test_CA04_check_item_in_cart(driver_logged):
    productos = driver_logged.find_elements(By.CLASS_NAME, "inventory_item")
    primerProducto = productos [0]
    nombreInv = str(primerProducto.find_element(By.CLASS_NAME, "inventory_item_name").text)
    precioInv = str(primerProducto.find_element(By.CLASS_NAME, "inventory_item_price").text)
    descrpInv = str(primerProducto.find_element(By.CLASS_NAME, "inventory_item_desc").text)
    agregar_al_carrito(driver_logged, 0)
    ir_al_carrito(driver_logged)
    productoEnCarrito = driver_logged.find_element(By.CLASS_NAME, "cart_item")
    nombreCar = str(productoEnCarrito.find_element(By.CLASS_NAME, "inventory_item_name").text)
    precioCar = str(productoEnCarrito.find_element(By.CLASS_NAME, "inventory_item_price").text)
    descrpCar = str(productoEnCarrito.find_element(By.CLASS_NAME, "inventory_item_desc").text)
    assert nombreInv == nombreCar, "El nombre del producto en el catálogo difiere al del carrito"
    assert precioInv == precioCar, "El precio del producto en el catálogo difiere al del carrito"
    assert descrpInv == descrpCar, "La descripción del producto en el catálogo difiere a la del carrito"
