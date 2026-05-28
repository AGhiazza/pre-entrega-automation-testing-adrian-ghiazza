from pages.InventoryPage import InventoryPage

def test_IN01_title_validation(driver_logged):  #Caso para validar el titulo de la pagina
    titulo = driver_logged.title                #.title obtiene el título de la pestaña del navegador y en este caso lo guarda en la variable "titulo"
    assert "Swag Labs" in titulo, "El título de la página es incorrecto." #verifica que "Swag Labs" esté contenido en el titulo

def test_IN02_prods_in_catalog(driver_logged):  #Caso para validar que se vean productos
    inventory_page = InventoryPage(driver_logged)
    productos = inventory_page.obtener_productos()
    assert len(productos) > 0, "No se visualizan productos en la pagina." #verifica que la cantidad de resultados de la busqueda sea mayor a 0

def test_IN03_ui_validation(driver_logged):     #Caso para buscar diversos elementos en la UI y verificar que sean visibles
    inventory_page = InventoryPage(driver_logged)
    hamburguesa = inventory_page.obtener_hamburguesa()    #a diferencia de elementS que hace una lista de todos los elementos que encuentre, 
                                                                                #find_element guarda el primer elemento que encuentra directamente
    filtro = inventory_page.obtener_ordenar ()
    carrito = inventory_page.obtener_carrito ()
    assert hamburguesa.is_displayed() , "No se visualiza el icono hamburguesa"  #se usa el metodo .is_displayed() para verificar que el elemento sea visible en la pagina
    assert filtro.is_displayed(), "No se visualiza el icono de filtro"
    assert carrito.is_displayed(), "No se visualiza el icono de carrito"

def test_IN04_product_validation(driver_logged):    #Caso para validar que el nombre y precio del producto se visualice (tomando el primer producto que encuentre)
    inventory_page = InventoryPage(driver_logged)
    
    nombre = inventory_page.obtener_nombre_producto(0)
    precio = inventory_page.obtener_precio_producto(0)
    print(f"Nombre: {nombre} | Precio: {precio}") #imprime los valores recuperados para nombre y precio con la variable .text
    assert nombre != "", "No se visualiza el nombre del primer producto" #Verifica que contenga un valor
    assert precio != "", "No se visualiza el precio del primer producto"