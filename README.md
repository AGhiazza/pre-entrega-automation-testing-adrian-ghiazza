# TalentoTech - Comisión 26143 - Automatización QA - Adrian Ghiazza

## Descripción



## Propósito del Proyecto

El objetivo de este proyecto es aprender tecnologías y procesos de automatización QA. Para ello se automatiza el sitio web [saucedemo.com](https://www.saucedemo.com), una aplicación demo diseñada especialmente para prácticas de testing.

## Tecnologías y Herramientas Utilizadas

- **Python** - Lenguaje principal
- **Pytest** - Framework de testing
- **Selenium WebDriver** - Automatización del navegador
- **Requests** - Consumo y testing de APIs
- **pytest-html** - Generación de reportes HTML
- **Logging** - Sistema de registros de ejecución
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
clase_16.9_EntregaFinal/
├── pages/                          # Page Objects Model para UI
│   ├── BasePage.py                # Clase base con selectores y métodos comunes
│   ├── LoginPage.py               # Página de login
│   ├── InventoryPage.py           # Página de catálogo de productos
│   └── CartPage.py                # Página del carrito
├── tests_ui/                       # Tests de interfaz de usuario
│   ├── test_login.py              # Tests de login (LO01, LO02)
│   ├── test_login_CSV.py          # Tests parametrizados de login (LO01 x3)
│   ├── test_inventario.py         # Tests de inventario (IN01-IN04)
│   └── test_carrito.py            # Tests de carrito (CA01-CA05)
├── tests_api/                      # Tests de API
│   ├── test_login_api.py          # Tests de autenticación API (APILO01-APILO02)
│   └── test_users_api.py          # Tests de usuarios API (APIUS01-APIUS03)
├── data/                           # Datos de prueba
│   ├── users.csv                  # Credenciales parametrizadas
│   ├── login_cases.json           # Casos de login para API
│   └── products.json              # Lista de Productos para verificación
├── utils/                          # Utilidades compartidas
│   ├── data_reader.py             # Lector genérico de datos (CSV, JSON)
│   ├── logger.py                  # Configuración del sistema de logging
│   └── api_utils.py               # Configuración de APIs (URL base, headers)
├── reports/                        # Reportes generados
│   ├── screenshots/               # Capturas de pantalla en fallos
│   └── logs/                       # Archivos de log con timestamps
├── conftest.py                     # Configuración de pytest y fixtures
├── pytest.ini                      # Configuración de pytest
├── .gitignore                      # Archivos a ignorar en Git
├── requirements.txt                # Dependencias del proyecto
├── README.md                       # Este archivo
├── selectors.md                    # Referencia de selectores por página
└── testcaseslist.md               # Documentación de casos de prueba
```


## Casos de Prueba

### UI - Login
| ID | Descripción | Datos |
|----|-------------|-------|
| LO01 | Login exitoso | standard_user / secret_sauce |
| LO02 | Login fallido sin campos | - (campos vacíos) |
| LO01 (parametrizado) | Login - caso válido | CSV fila 1 |
| LO01 (parametrizado) | Login - usuario inválido | CSV fila 2 |
| LO01 (parametrizado) | Login - contraseña inválida | CSV fila 3 |

### UI - Inventario
| ID | Descripción |
|----|-------------|
| IN01 | Verificar título de la página |
| IN02 | Comprobar visibilidad de productos |
| IN03 | Validar elementos de UI (menú, filtros, carrito) |
| IN04 | Validar nombre y precio del producto |

### UI - Carrito
| ID | Descripción |
|----|-------------|
| CA01 | Badge de carrito visible al agregar |
| CA02 | Contador incremental con múltiples productos |
| CA03 | Navegación a carrito funciona |
| CA04 | Datos de producto coinciden entre inventario y carrito |
| CA05 | Validar productos del JSON en carrito |

### API - Login
| ID | Descripción | Esperado |
|----|-------------|----------|
| APILO01 | Login exitoso | 200 + token |
| APILO02 | Login sin contraseña | 400 |

### API - Usuarios
| ID | Descripción | Método |
|----|-------------|--------|
| APIUS01 | Obtener usuario | GET |
| APIUS02 | Crear usuario | POST |
| APIUS03 | Eliminar usuario | DELETE |


## Ejecución de Pruebas

### Todos los tests
```bash
pytest -v
```

### Solo tests de UI
```bash
pytest -m ui -v
```

### Solo tests de API
```bash
pytest -m api -v
```

### Tests específicos
```bash
# Usar el nombre del archivo correspondiente
pytest tests_ui/test_login.py -v
```

## Opciones útiles

| Opción | Descripción |
|--------|-------------|
| `-v` | Modo verbose, muestra el nombre de cada test y su resultado |
| `-s` | Muestra los `print()` en la consola durante la ejecución |
| `--html=ruta` | Genera un reporte HTML con los resultados |

Se pueden combinar, por ejemplo: `pytest testcases -v -s --html=reports/reporte.html`


## Generar reporte HTML:

### Reporte HTML
- Ubicación: `reports/reporte.html`
- Contiene: Resultado de cada test, duración, capturas en fallos
- Comando: `pytest --html=reporte.html --self-contained-html`

### Logs
- Ubicación: `logs/log_YYYY-MM-DD_HH-MM-SS.log`
- Contiene: Cada acción de los tests con timestamp
- Útil para: Depuración post-ejecución

### Capturas de Pantalla
- Ubicación: `reports/screenshots/`
- Se genera: Solo cuando un test falla
- Formato: PNG con timestamp

## Notas Importantes

- Los tests de UI requieren **Chrome instalado** en el sistema
- El proyecto usa **encoding UTF-8** para soportar caracteres especiales
- Las rutas se construyen con `pathlib` para compatibilidad multiplataforma (Windows/Linux/Mac)
- El fixture `driver_logged` busca el primer usuario con `"valido": "true"` en el CSV
- El logging se inicializa automáticamente al importar `logger.py`
- Las capturas de pantalla se toman automáticamente solo cuando un test falla