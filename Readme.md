# Pre-Entrega Proyecto Automatización QA - SauceDemo

Proyecto realizado con Selenium, Python aplicando Page Obejt Model (POM).

# Casos Automatizados 
- Login exitoso
- Login Validado
- Validacion de campos vacios
- Verificacion de catalogo 
- validacion de productos visibles 
- validacion de elementos de interfaz

# Tecnologias Usadas
- Python
- Selenium
- Pytest
- Webdriver Manager

# para antes de ejecutar las pruebas se necesita tener instaladas estas dependencias
- selenium
- pytest
- pytest-html
- webdriver-manager

# Instrucciones de instalacion de dependencias 
- Para instalar la libreria Selenium: pip install selenium
    -   con este comando podes ver la version instalada: pip show selenium
    -   con este comando muestra todos los paquetes instalados en tu entorno python: pip freeze
- Para instalar la libreria pytest: python -m pip install pytest
- Para instalar pytest-html: pip install pytest-html
- para instalar webdriver-manager: pip install webdriver-manager

# Ejecucuion
Ejecución de los test: python -m pytest
Generación de reporte: pytest tests/test_saucedemo.py -v --html=reports/reporte.html