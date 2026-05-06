from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SauceLoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.saucedemo.com"
        
        # Selectores de la página de Login
        self.username_input = (By.ID, "user-name")
        self.password_input = (By.ID, "password")
        self.login_button = (By.ID, "login-button")
        self.error_container = (By.CSS_SELECTOR, "h3[data-test='error']")

    def ingresar_a_la_web(self):
        self.driver.get(self.url)

    def realizar_login(self, usuario, contrasenia):
        wait = WebDriverWait(self.driver, 10)
        
        # Escribir usuario si está presente
        user_field = wait.until(EC.presence_of_element_located(self.username_input))
        user_field.clear()
        if usuario: # Solo escribe si no se envía vacío
            user_field.send_keys(usuario)
            
        # Escribir contraseña si está presente
        pass_field = wait.until(EC.presence_of_element_located(self.password_input))
        pass_field.clear()
        if contrasenia: # Solo escribe si no se envía vacío
            pass_field.send_keys(contrasenia)
            
        # Clic en el botón
        wait.until(EC.element_to_be_clickable(self.login_button)).click()

    def obtener_mensaje_error(self):
        wait = WebDriverWait(self.driver, 5)
        error_element = wait.until(EC.visibility_of_element_located(self.error_container))
        return error_element.text


class SauceInventoryPage:
    def __init__(self, driver):
        self.driver = driver
        
        # Selectores de la página de Inventario / Catálogo
        self.app_logo = (By.CLASS_NAME, "app_logo")                 # Título Swag Labs
        self.title_label = (By.CLASS_NAME, "title")                 # Subtítulo Products
        self.inventory_items = (By.CLASS_NAME, "inventory_item")    # Caja de cada producto
        self.item_name = (By.CLASS_NAME, "inventory_item_name")
        self.item_price = (By.CLASS_NAME, "inventory_item_price")
        self.add_to_cart_btn = (By.CSS_SELECTOR, ".btn_primary.btn_inventory")
        self.shopping_cart = (By.CLASS_NAME, "shopping_cart_link")
        self.filter_dropdown = (By.CLASS_NAME, "product_sort_container")

    def verificar_url_inventario(self):
        wait = WebDriverWait(self.driver, 10)
        return wait.until(EC.url_contains("/inventory.html"))

    def obtener_titulo_principal(self):
        return self.driver.find_element(*self.app_logo).text

    def obtener_subtitulo(self):
        return self.driver.find_element(*self.title_label).text

    def contar_productos_visibles(self):
        return len(self.driver.find_elements(*self.inventory_items))

    def obtener_datos_primer_producto(self):
        productos = self.driver.find_elements(*self.inventory_items)
        
        primer_producto = productos[0]
        
        nombre = primer_producto.find_element(By.CLASS_NAME, "inventory_item_name").text
        precio = primer_producto.find_element(By.CLASS_NAME, "inventory_item_price").text
        
        return nombre, precio

    def elementos_interfaz_presentes(self):
        try:
            carrito = self.driver.find_element(*self.shopping_cart).is_displayed()
            filtro = self.driver.find_element(*self.filter_dropdown).is_displayed()
            boton_agregar = self.driver.find_element(*self.add_to_cart_btn).is_displayed()
            return carrito and filtro and boton_agregar
        except:
            return False

  