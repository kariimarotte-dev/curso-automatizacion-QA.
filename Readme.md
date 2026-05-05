# Pre-Entrega Proyecto Automatización QA - SauceDemo

Este repositorio contiene la primera etapa de automatización para la plataforma **SauceDemo**, cubriendo las consignas e interacciones vistas hasta la **Clase 8**.

## Estructura del Proyecto
El diseño aplica el patrón **Page Object Model (POM)** para mantener los componentes separados del código de prueba:
- `pages/sauce_pages.py`: Contiene los localizadores y métodos de interacción de la interfaz.
- `tests/test_saucedemo.py`: Contiene las pruebas y las aserciones de Pytest.

## Requisitos e Instalación
1. Clonar el repositorio.
2. Instalar las dependencias del sistema:
   ```bash
   pip install selenium pytest webdriver-manager