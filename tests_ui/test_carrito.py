import pytest
from pages.InventoryPage import InventoryPage
from pages.CartPage import CartPage
from utils.data_reader import read_json_files
from utils.logger import logger
import pytest_check as check
from utils.config import CART_PATH

@pytest.mark.ui
def test_CA01_cart_badge(driver_logged):    #Caso para verificar que se muestre el numero de productos cuando se agrega al menos 1 al carrito
    logger.info("=== Iniciando test_CA01_cart_badge ===")
    inventory_page = InventoryPage(driver_logged)
    logger.info("Agregando producto al carrito")
    inventory_page.agregar_al_carrito(0)
    
    logger.info("Obteniendo contador del carrito")
    carritoBadge = inventory_page.obtener_badge_carrito() #busca el elemento de la marca de cantidad de prodcutos en el carrito y lo guarda en la variable
    logger.info("Verificando contador sea visible")
    assert carritoBadge.is_displayed(), "No se visualiza badge del carrito"

@pytest.mark.ui
def test_CA02_cart_badge_increase(driver_logged):   #Caso para agregar 2 productos al carrito y ver que el contador suba.
    logger.info("=== Iniciando test_CA02_cart_badge_increase ===")
    inventory_page = InventoryPage(driver_logged)
    logger.info("Agregando producto al carrito")
    inventory_page.agregar_al_carrito(0)
    logger.info("Agregando producto al carrito")
    inventory_page.agregar_al_carrito(1)
    logger.info("Obteniendo cantidad de productos en el carrito")
    carritoBadge = inventory_page.obtener_cantidad_carrito()
    carritoBadgeNum = int(carritoBadge)    #Toma el texto en la variable del contador del carrito y lo convierte en integer para despues comparar
    print(f"Cantidad de Productos en el carrito: {carritoBadgeNum}")    
    logger.info("Verificando cantidad correcta de productos en el carrito")
    assert carritoBadgeNum == 2, "No se visualiza la cantidad correcta de productos en el icono del carrito"

@pytest.mark.ui
def test_CA03_go_to_cart(driver_logged):    #Caso para validar que cuando se navega al carrito se visualice la pagina correcta.
    logger.info("=== Iniciando test_CA03_go_to_cart ===")
    inventory_page = InventoryPage(driver_logged)
    logger.info("Yendo al carrito")
    inventory_page.ir_al_carrito()
    logger.info("Verificando navegación al carrito")
    assert CART_PATH in driver_logged.current_url, "No se visualiza la pagina del carrito"   

@pytest.mark.ui
def test_CA04_check_item_in_cart(driver_logged):    #Caso para validar que las caracteristicas de un producto sean iguales en el inventario como en el carrito
    logger.info("=== Iniciando test_CA04_check_item_in_cart ===")
    inventory_page = InventoryPage(driver_logged)
    cart_page = CartPage(driver_logged)
    
    logger.info("Obteniendo datos del producto en inventario")
    nombreInv = str(inventory_page.obtener_nombre_producto(0)) 
    descrpInv = str(inventory_page.obtener_descripcion_producto(0)) 
    precioInv = str(inventory_page.obtener_precio_producto(0))
    logger.info("Agregando producto al carrito")
    inventory_page.agregar_al_carrito(0)
    logger.info("Yendo al carrito")
    inventory_page.ir_al_carrito()
    logger.info("Obteniendo datos del producto en carrito")
    nombreCar = str(cart_page.obtener_nombre_producto(0))  
    descrpCar = str(cart_page.obtener_descripcion_producto(0))
    precioCar = str(cart_page.obtener_precio_producto(0))
    logger.info("Comparando valores de Inventario vs Carrito")
    check.equal (nombreInv, nombreCar, "El nombre del producto en el catálogo difiere al del carrito")
    check.equal (precioInv, precioCar, "El precio del producto en el catálogo difiere al del carrito")
    check.equal (descrpInv, descrpCar, "La descripción del producto en el catálogo difiere a la del carrito")

@pytest.mark.ui
def test_CA05_check_item_name(driver_logged):       # Caso para validar que los productos en products.json se agreguen y aparezcan correctamente en el carrito
    logger.info("=== Iniciando test_CA05_check_item_name ===")
    inventory_page = InventoryPage(driver_logged)
    cart_page = CartPage(driver_logged)
    logger.info("Obteniendo lista de productos del Json")
    listaProducJson = read_json_files("products.json")
    logger.info("Agregando productos de la lista al carrito")
    for producto in listaProducJson:
        inventory_page.agregar_producto_por_nombre(producto["nombre"])

    logger.info("Yendo al carrito")    
    inventory_page.ir_al_carrito()
    logger.info("Obteniendo lista de productos en el carrito")    
    productosCarrito = cart_page.obtener_productos()
    
    logger.info("Comparando productos en Json vs carrito")
    for productoJson in listaProducJson: # Loop de productos en Json
        encontrado = False # Cambia "encontrado" a FALSE por default para que el assert falle en caso de no encotrar el producto
        for productoCarrito in productosCarrito: # Loop de productos en carrito
            if (productoCarrito.find_element(*cart_page.cart_item_name).text == productoJson["nombre"]): # Compara los nombres y si matchean, pasa encontrado a "True"
                encontrado = True
                break
        assert encontrado, f"Producto incorrecto o faltante: {productoJson["nombre"]}"
