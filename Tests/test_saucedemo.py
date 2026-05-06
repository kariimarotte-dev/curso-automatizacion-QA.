import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from sauce_pages import SauceLoginPage, SauceInventoryPage

@pytest.fixture
def driver():
    # Setup: Inicializar el navegador de forma dinámica
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(service=service, options=options)
    
    yield driver
    
    # Teardown: Cerrar el navegador al finalizar cada test
    driver.quit()


# --- CASOS DE PRUEBA DE LOGIN ---

def test_caso_1_login_exitoso(driver):
    login_page = SauceLoginPage(driver)
    inventory_page = SauceInventoryPage(driver)
    
    login_page.ingresar_a_la_web()
    login_page.realizar_login("standard_user", "secret_sauce")
    
    # Validaciones obligatorias de la consigna
    assert inventory_page.verificar_url_inventario(), "No se redirigió a /inventory.html"
    assert inventory_page.obtener_titulo_principal() == "Swag Labs", "El título de la app no coincide"


def test_caso_2_login_invalido(driver):
    login_page = SauceLoginPage(driver)
    
    login_page.ingresar_a_la_web()
    login_page.realizar_login("usuario_invalido", "clave_invalida")
    
    error_text = login_page.obtener_mensaje_error()
    assert "Username and password do not match any user in this service" in error_text


def test_caso_3_campos_vacios(driver):
    login_page = SauceLoginPage(driver)
    
    login_page.ingresar_a_la_web()
    login_page.realizar_login("", "") # Credenciales vacías
    
    error_text = login_page.obtener_mensaje_error()
    assert "Username is required" in error_text


# --- CASOS DE PRUEBA DE NAVEGACIÓN Y CATÁLOGO (CLASES 6 A 8) ---

def test_casos_4_al_10_verificacion_catalogo(driver):
    login_page = SauceLoginPage(driver)
    inventory_page = SauceInventoryPage(driver)
    
    # Paso previo: Loguearse para ver el catálogo
    login_page.ingresar_a_la_web()
    login_page.realizar_login("standard_user", "secret_sauce")
    
    # Caso 4 & 5: Verificar títulos visibles en el catálogo
    assert inventory_page.obtener_subtitulo() == "Products", "El subtítulo del catálogo no es legible o correcto"
    
    # Caso 6: Comprobar presencia de productos en la grilla (Al menos uno)
    cantidad_productos = inventory_page.contar_productos_visibles()
    assert cantidad_productos > 0, "No se encontraron productos visibles en el catálogo"
    
    # Criterio Mínimo Exigido: Listar nombre y precio del primero
    nombre_primero, precio_primero = inventory_page.obtener_datos_primer_producto()
    print(f"\n[INFO] Primer Producto: {nombre_primero} | Precio: {precio_primero}")
    assert len(nombre_primero) > 0, "El nombre del primer producto está vacío"
    assert "$" in precio_primero, "El formato del precio no contiene el símbolo '$'"
    
    # Casos 8, 9 & 10: Validar elementos cruciales de la interfaz
    assert inventory_page.elementos_interfaz_presentes(), "Faltan elementos importantes en la interfaz (Carrito, Filtro o Botones)"