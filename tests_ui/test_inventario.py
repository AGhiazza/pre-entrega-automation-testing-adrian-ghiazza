import pytest
from pages.InventoryPage import InventoryPage
from utils.logger import logger
import pytest_check as check

@pytest.mark.ui
def test_IN01_title_validation(driver_logged):  #Caso para validar el titulo de la pagina
    logger.info("=== Iniciando test_IN01_title_validation ===")
    titulo = driver_logged.title                #.title obtiene el título de la pestaña del navegador y en este caso lo guarda en la variable "titulo"
    logger.info("Chequeando el títlo de la pagina.")
    assert "Swag Labs" in titulo, "El título de la página es incorrecto." #verifica que "Swag Labs" esté contenido en el titulo

@pytest.mark.ui
def test_IN02_prods_in_catalog(driver_logged):  #Caso para validar que se vean productos
    logger.info("=== Iniciando test_IN02_prods_in_catalog ===")
    inventory_page = InventoryPage(driver_logged)
    logger.info("Obteniendo productos de la pagina")
    productos = inventory_page.obtener_productos()
    logger.info("Verificando cantidad de productos en la página")
    assert len(productos) > 0, "No se visualizan productos en la pagina." #verifica que la cantidad de resultados de la busqueda sea mayor a 0

@pytest.mark.ui
def test_IN03_ui_validation(driver_logged):     #Caso para buscar diversos elementos en la UI y verificar que sean visibles
    logger.info("=== Iniciando test_IN03_ui_validation ===")
    inventory_page = InventoryPage(driver_logged)
    logger.info("Verificando menú hamburguesa")
    hamburguesa = inventory_page.obtener_hamburguesa()    #a diferencia de elementS que hace una lista de todos los elementos que encuentre, 
                                                                                #find_element guarda el primer elemento que encuentra directamente
    logger.info("Verificando botón ordenar")
    filtro = inventory_page.obtener_ordenar ()
    logger.info("Verificando botón carrito")
    carrito = inventory_page.obtener_carrito ()
    check.is_true(hamburguesa.is_displayed() , "No se visualiza el icono hamburguesa")  #se usa el metodo .is_displayed() para verificar que el elemento sea visible en la pagina
    check.is_true (filtro.is_displayed(), "No se visualiza el icono de filtro")
    check.is_true (carrito.is_displayed(), "No se visualiza el icono de carrito")

@pytest.mark.ui
def test_IN04_product_validation(driver_logged):    #Caso para validar que el nombre y precio del producto se visualice (tomando el primer producto que encuentre)
    logger.info("=== Iniciando test_IN04_product_validation ===")
    inventory_page = InventoryPage(driver_logged)
    
    logger.info("Obteniendo nombre de producto")
    nombre = inventory_page.obtener_nombre_producto(0)
    logger.info("Obteniendo precio de producto")
    precio = inventory_page.obtener_precio_producto(0)
    print(f"Nombre: {nombre} | Precio: {precio}") #imprime los valores recuperados para nombre y precio con la variable .text
    check.is_true (nombre != "", "No se visualiza el nombre del primer producto") #Verifica que contenga un valor
    check.is_true (precio != "", "No se visualiza el precio del primer producto")