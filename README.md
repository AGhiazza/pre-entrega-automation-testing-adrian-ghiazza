# TalentoTech - Comisión 26143 - Automomatización QA - Adrian Ghiazza

## Descripción



## Propósito del Proyecto

El objetivo de este proyecto es aprender tecnologías y procesos de automatización QA. Para ello se automatiza el sitio web [saucedemo.com](https://www.saucedemo.com), una aplicación demo diseñada especialmente para prácticas de testing.

## Tecnologías Utilizadas

- **Python** - Lenguaje principal
- **Pytest** - Framework de testing
- **Selenium WebDriver** - Automatización del navegador
- **webdriver-manager** - Gestión automática del ChromeDriver
- **Claude Sonnet 4.6 (Anthropic)** - Corrección de errores y revisión de buenas prácticas
- **Git / GitHub** - Control de versiones


## Instalación de Dependencias

1. Instalar [Python](https://www.python.org/downloads/) y [Visual Studio Code](https://code.visualstudio.com/).
2. Abrir la carpeta raíz del proyecto en Visual Studio Code.
3. Abrir una terminal (`Terminal > Nueva Terminal`) y ejecutar el siguientes comando para instalar todas las dependencias:

```bash
pip install -r requirements.txt
```


## Estructura del Proyecto

```
├── conftest.py               # Fixtures compartidos (driver, login)
├── funcAux/
│   ├── LoginPage.py          # Función de login
│   └── InventoryPage.py      # Funciones de agregar al carrito e ir al carrito
├── testcases/
│   ├── test_login.py         # Casos de prueba: Login (LO01-LO05)
│   ├── test_inventario.py    # Casos de prueba: Inventario (IN01-IN04)
│   └── test_carrito.py       # Casos de prueba: Carrito (CA01-CA04)
├── selectors.md              # Referencia de selectores CSS/ID por página
└── testcaseslist.md          # Lista de casos de prueba
```


## Casos de Prueba

| ID | Descripción |
|----|-------------|
| LO01 | Login exitoso con credenciales válidas |
| IN01 | Verificar título correcto de la página de inventario |
| IN02 | Comprobar que existan productos visibles |
| IN03 | Validar presencia de elementos de interfaz (menú, filtros, carrito) |
| IN04 | Verificar nombre y precio del primer producto |
| CA01 | Agregar un producto y verificar que aparezca el badge del carrito |
| CA02 | Agregar dos productos y verificar que el contador incremente correctamente |
| CA03 | Navegar al carrito y verificar la redirección correcta |
| CA04 | Verificar que el producto agregado aparezca correctamente en el carrito |


## Ejecución de las Pruebas

**Todos los tests:**
```bash
pytest clase_16.9_EntregaFinal/testcases -v
```

**Por módulo:**
```bash
pytest clase_16.9_EntregaFinal/testcases/test_login.py -v
pytest clase_16.9_EntregaFinal/testcases/test_inventario.py -v
pytest clase_16.9_EntregaFinal/testcases/test_carrito.py -v
```


## Opciones útiles de Pytest

| Opción | Descripción |
|--------|-------------|
| `-v` | Modo verbose, muestra el nombre de cada test y su resultado |
| `-s` | Muestra los `print()` en la consola durante la ejecución |
| `--html=ruta` | Genera un reporte HTML con los resultados |

Se pueden combinar, por ejemplo: `pytest testcases -v -s --html=reports/reporte.html`


## Generar reporte HTML:

```bash
pytest clase_16.9_EntregaFinal/testcases -v --html=reports/reporte.html
```
> **Nota:** Usar `--self-contained-html` para generar un reporte independiente que no requiera la carpeta `assets`:
> ```
> pytest clase_16.9_EntregaFinal/testcases -v --html=clase_16.9_EntregaFinal/reports/reporte.html --self-contained-html
> ```