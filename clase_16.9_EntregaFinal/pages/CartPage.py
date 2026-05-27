from selenium.webdriver.common.by import By

class CartPage:
    def __init__(self, driver):
        
        self.driver = driver

        #Selectores
        self.app_logo = (By.CLASS_NAME, "app_logo")
        self.your_cart_title = (By.CLASS_NAME, "title")

        self.cart_list = (By.CLASS_NAME, "cart_list")
        self.cart_item_container = (By.CLASS_NAME, "cart_item")
        self.cart_item_qty = (By.CLASS_NAME, "cart_quantity")
        self.cart_item_details = (By.CLASS_NAME, "cart_item_label")
        self.cart_item_name = (By.CLASS_NAME, "inventory_item_name")
        self.cart_item_desc = (By.CLASS_NAME, "inventory_item_desc")
        self.cart_item_price = (By.CLASS_NAME, "inventory_item_price")
        self.remove_button = (By.CSS_SELECTOR, "[data-test^='remove']") #El ^= significa "que empiece con", así agarra cualquier botón remove sin importar el producto.

        self.continue_shopping = (By.ID, "continue-shopping")
        self.checkout = (By.ID, "checkout")

