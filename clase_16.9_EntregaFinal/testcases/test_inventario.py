from selenium.webdriver.common.by import By


def test_IN01_title_validation(driver_logged):  #Caso para validar el titulo de la pagina
    titulo = driver_logged.title                #.title obtiene el título de la pestaña del navegador y en este caso lo guarda en la variable "titulo"
    assert "Swag Labs" in titulo, "El título de la página es incorrecto." #verifica que "Swag Labs" esté contenido en el titulo

def test_IN02_prods_in_catalog(driver_logged):  #Caso para validar que se vean productos
    productos = driver_logged.find_elements(By.CLASS_NAME, "inventory_item") #Busca todos los elementos con la clase "inventory_item"
    assert len(productos) > 0, "No se visualizan productos en la pagina." #verifica que la cantidad de resultados de la busqueda sea mayor a 0

def test_IN03_ui_validation(driver_logged):     #Caso para buscar diversos elementos en la UI y verificar que sean visibles
    hamburguesa = driver_logged.find_element(By.ID, "react-burger-menu-btn")    #a diferencia de elementS que hace una lista de todos los elementos que encuentre, 
                                                                                #find_element guarda el primer elemento que encuentra directamente
    filtro = driver_logged.find_element(By.CLASS_NAME, "product_sort_container")
    carrito = driver_logged.find_element(By.CLASS_NAME, "shopping_cart_link")
    assert hamburguesa.is_displayed() , "No se visualiza el icono hamburguesa"  #se usa el metodo .is_displayed() para verificar que el elemento sea visible en la pagina
    assert filtro.is_displayed(), "No se visualiza el icono de filtro"
    assert carrito.is_displayed(), "No se visualiza el icono de carrito"

def test_IN04_product_validation(driver_logged):    #Caso para validar que el nombre y precio del producto se visualice (tomando el primer producto que encuentre)
    productos = driver_logged.find_elements(By.CLASS_NAME, "inventory_item") #Busca todos los elementos con la clase "inventory_item"
    primerProducto = productos [0]  #selecciona el primer elemento de la lista "productos" y lo guarda en "primerProducto"
    nombre = primerProducto.find_element(By.CLASS_NAME, "inventory_item_name")
    precio = primerProducto.find_element(By.CLASS_NAME, "inventory_item_price")
    print(f"Nombre: {nombre.text} | Precio: {precio.text}") #imprime los valores recuperados para nombre y precio con la variable .text
    assert nombre.is_displayed(), "No se visualiza el nombre del primer producto"
    assert precio.is_displayed(), "No se visualiza el precio del primer producto"