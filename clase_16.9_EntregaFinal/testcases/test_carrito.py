from pages.InventoryPage import InventoryPage
from pages.CartPage import CartPage

def test_CA01_cart_badge(driver_logged):    #Caso para verificar que se muestre el numero de productos cuando se agrega al menos 1 al carrito
    inventory_page = InventoryPage(driver_logged)
    inventory_page.agregar_al_carrito(0)
    
    carritoBadge = inventory_page.obtener_badge_carrito() #busca el elemento de la marca de cantidad de prodcutos en el carrito y lo guarda en la variable
    assert carritoBadge.is_displayed(), "No se visualiza badge del carrito"

def test_CA02_cart_badge_increase(driver_logged):   #Caso para agregar 2 productos al carrito y ver que el contador suba.
    inventory_page = InventoryPage(driver_logged)
    inventory_page.agregar_al_carrito(0)
    inventory_page.agregar_al_carrito(1)
    carritoBadge = inventory_page.obtener_cantidad_carrito()
    carritoBadgeNum = int(carritoBadge)    #Toma el texto en la variable del contador del carrito y lo convierte en integer para despues comparar
    print(f"Cantidad de Productos en el carrito: {carritoBadgeNum}")    #Imprime por consola la cantidad de productos agregados
    assert carritoBadgeNum == 2, "No se visualiza la cantidad correcta de productos en el icono del carrito"    #valida que la cantidad de prodcutos sea igual a 2

def test_CA03_go_to_cart(driver_logged):    #Caso para validar que cuando se navega al carrito se visualice la pagina correcta.
    inventory_page = InventoryPage(driver_logged)
    inventory_page.ir_al_carrito()
    assert "/cart.html" in driver_logged.current_url, "No se visualiza la pagina del carrito"   

def test_CA04_check_item_in_cart(driver_logged):    #Caso para validar que las caracteristicas de un producto sean iguales en el inventario como en el carrito
    inventory_page = InventoryPage(driver_logged)
    cart_page = CartPage(driver_logged)
    
    
    nombreInv = str(inventory_page.obtener_nombre_producto(0)) #Guarda el nombre del producto en el inventario.
    descrpInv = str(inventory_page.obtener_descripcion_producto(0)) #Guarda la descripción del producto en el inventario.
    precioInv = str(inventory_page.obtener_precio_producto(0)) #Guarda el precio del producto en el inventario.
    inventory_page.agregar_al_carrito(0)
    inventory_page.ir_al_carrito()
    nombreCar = str(cart_page.obtener_nombre_producto(0))  #Guarda el nombre del producto en el carrito.
    descrpCar = str(cart_page.obtener_descripcion_producto(0))
    precioCar = str(cart_page.obtener_precio_producto(0))
    assert nombreInv == nombreCar, "El nombre del producto en el catálogo difiere al del carrito"   #Compara los nombres del producto fuera en el invetorio contra los del carrito
    assert precioInv == precioCar, "El precio del producto en el catálogo difiere al del carrito"
    assert descrpInv == descrpCar, "La descripción del producto en el catálogo difiere a la del carrito"