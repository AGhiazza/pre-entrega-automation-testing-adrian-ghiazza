from selenium.webdriver.common.by import By


def test_IN01_title_validation(driver_logged):
    titulo = driver_logged.title
    assert "Swag Labs" in titulo, "El título de la página es incorrecto."

def test_IN02_prods_in_catalog(driver_logged):
    productos = driver_logged.find_elements(By.CLASS_NAME, "inventory_item")
    assert len(productos) > 0, "No se visualizan productos en la pagina."

def test_IN03_ui_validation(driver_logged):
    hamburguesa = driver_logged.find_element(By.ID, "react-burger-menu-btn")
    filtro = driver_logged.find_element(By.CLASS_NAME, "product_sort_container")
    carrito = driver_logged.find_element(By.CLASS_NAME, "shopping_cart_link")
    assert hamburguesa.is_displayed() , "No se visualiza el icono hamburguesa"
    assert filtro.is_displayed(), "No se visualiza el icono de filtro"
    assert carrito.is_displayed(), "No se visualiza el icono de carrito"

def test_IN04_product_validation(driver_logged):
    productos = driver_logged.find_elements(By.CLASS_NAME, "inventory_item")
    primerProducto = productos [0]
    nombre = primerProducto.find_element(By.CLASS_NAME, "inventory_item_name")
    precio = primerProducto.find_element(By.CLASS_NAME, "inventory_item_price")
    print(f"Nombre: {nombre.text} | Precio: {precio.text}")
    assert nombre.is_displayed(), "No se visualiza el nombre del primer producto"
    assert precio.is_displayed(), "No se visualiza el precio del primer producto"