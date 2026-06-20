# TalentoTech - Comisión 26143 - Automatización QA - Adrian Ghiazza

![CI Status](https://github.com/AGhiazza/TT26143-Automation-Framework-Saucedemo/actions/workflows/ci.yml/badge.svg)

## Descripción

El objetivo de este proyecto es aprender tecnologías y procesos de automatización QA. Para ello se crea un Framework de automatización integral que combina pruebas de UI con Selenium, pruebas de API con Requests y pruebas BDD con Behave/Gherkin. El proyecto automatiza el sitio web [saucedemo.com](https://www.saucedemo.com), una aplicación demo diseñada especialmente para prácticas de testing, aplicando patrones de diseño profesionales y buenas prácticas de la industria.

## Tecnologías y Herramientas Utilizadas

- **Python 3.14** - Lenguaje principal
- **Pytest 9.0** - Framework de testing
- **Selenium WebDriver** - Automatización del navegador
- **Requests 2.34** - Consumo y testing de APIs
- **Behave 1.3.3** - Framework de BDD (Behavior-Driven Development)
- **pytest-html 4.2** - Generación de reportes HTML
- **pytest-check 2.8** - Soft assertions (múltiples validaciones por test)
- **Faker 40.23** - Generación de datos dinámicos para pruebas
- **pytest-metadata 3.1** - Metadata en reportes HTML
- **Logging** - Sistema de registros de ejecución
- **webdriver-manager** - Gestión automática del ChromeDriver
- **GitHub Actions** - Pipeline de CI/CD automático
- **Claude Sonnet 4.6 (Anthropic)** - Asistencia en desarrollo
- **Git / GitHub** - Control de versiones

## Instalación de Dependencias

1. Instalar [Python](https://www.python.org/downloads/) (versión 3.10+) y [Visual Studio Code](https://code.visualstudio.com/).
2. Clonar el repositorio y abrir la carpeta raíz en VS Code.
3. Abrir una terminal (`Terminal > Nueva Terminal`) y ejecutar el siguiente comando para instalar todas las dependencias:

```bash
pip install -r requirements.txt
```

## Estructura del Proyecto

```
TT26143-Automation-Framework-Saucedemo/
├── .github/
│   └── workflows/
│       └── ci.yml                  # Pipeline de CI/CD con GitHub Actions
├── pages/                          # Page Object Model para UI
│   ├── BasePage.py                 # Clase base con selectores y métodos comunes
│   ├── LoginPage.py                # Página de login
│   ├── InventoryPage.py            # Página de catálogo de productos
│   └── CartPage.py                 # Página del carrito
├── tests_ui/                       # Tests de interfaz de usuario
│   ├── test_login.py               # Tests de login (LO01, LO02)
│   ├── test_login_CSV.py           # Tests parametrizados de login (LO01 x3)
│   ├── test_inventario.py          # Tests de inventario (IN01-IN04)
│   └── test_carrito.py             # Tests de carrito (CA01-CA05)
├── tests_api/                      # Tests de API REST
│   ├── test_login_api.py           # Tests de autenticación API (APILO01-APILO02)
│   └── test_users_api.py           # Tests de usuarios API (APIUS01-APIUS03)
├── features/                       # Tests BDD con Behave/Gherkin
│   ├── login.feature               # Escenarios de login en lenguaje Gherkin
│   ├── environment.py              # Setup y teardown de Behave
│   └── steps/
│       └── login_steps.py          # Implementación de los pasos Gherkin
├── data/                           # Datos de prueba
│   ├── users.csv                   # Credenciales parametrizadas
│   ├── login_cases.json            # Casos de login para API
│   └── products.json               # Lista de productos para verificación
├── utils/                          # Utilidades compartidas
│   ├── data_reader.py              # Lector genérico de datos (CSV, JSON)
│   ├── logger.py                   # Configuración del sistema de logging
│   └── api_utils.py                # Configuración de APIs (URL base, headers)
├── reports/                        # Reportes generados (autogenerado)
│   ├── reporte.html                # Reporte HTML de pytest
│   ├── screenshots/                # Capturas de pantalla en fallos
│   └── logs/                       # Archivos de log con timestamps
├── conftest.py                     # Fixtures y hooks compartidos
├── pytest.ini                      # Configuración de pytest
├── .gitignore                      # Archivos a ignorar en Git
├── requirements.txt                # Dependencias del proyecto
├── README.md                       # Este archivo
├── selectors.md                    # Referencia de selectores por página
└── testcaseslist.md                # Documentación de casos de prueba
```

## Patrones y Convenciones Implementadas

- **Page Object Model (POM)** con herencia de `BasePage` para reutilizar selectores y métodos comunes
- **Fixtures** reutilizables en `conftest.py` (`driver`, `driver_logged`)
- **Parametrización** con CSV y JSON para data-driven testing
- **Soft assertions** con `pytest-check` para múltiples validaciones por test
- **Datos dinámicos** con `Faker` para generación de datos realistas en tests de API
- **BDD** con Behave y Gherkin para escenarios legibles por negocio
- **Logging** con timestamps en `reports/logs/`
- **Capturas automáticas** en fallos integradas al reporte HTML

## Casos de Prueba

### UI - Login
| ID | Descripción | Datos |
|----|-------------|-------|
| LO01 | Login exitoso | standard_user / secret_sauce |
| LO02 | Login fallido sin campos | Campos vacíos |
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
| CA01 | Badge de carrito visible al agregar producto |
| CA02 | Contador incremental con múltiples productos |
| CA03 | Navegación al carrito funciona correctamente |
| CA04 | Datos de producto coinciden entre inventario y carrito |
| CA05 | Validar productos del JSON contra el carrito |

### API - Login (reqres.in)
| ID | Descripción | Método | Esperado |
|----|-------------|--------|----------|
| APILO01 | Login exitoso | POST | 200 + token |
| APILO02 | Login sin contraseña | POST | 400 |

### API - Usuarios (reqres.in)
| ID | Descripción | Método | Esperado |
|----|-------------|--------|----------|
| APIUS01 | Obtener usuario y validar tiempo de respuesta | GET | 200, < 2s |
| APIUS02 | Crear usuario con datos dinámicos (Faker) | POST | 201 |
| APIUS03 | Eliminar usuario | DELETE | 204 |

### BDD - Login (Behave/Gherkin)
| Escenario | Descripción |
|-----------|-------------|
| Login exitoso | Credenciales válidas redirigen al inventario |
| Login inválido (x5) | Distintas combinaciones inválidas muestran error correcto |

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

### Tests BDD con Behave
```bash
behave features/
```

### Tests específicos
```bash
pytest tests_ui/test_login.py -v
pytest tests_api/test_users_api.py -v
```

### Opciones útiles de pytest

| Opción | Descripción |
|--------|-------------|
| `-v` | Modo verbose, muestra el nombre de cada test y su resultado |
| `-s` | Muestra los `print()` en la consola durante la ejecución |
| `--html=ruta` | Genera un reporte HTML con los resultados |

## Reportes Generados

### Reporte HTML
- **Ubicación:** `reports/reporte.html`
- **Contiene:** Resultado de cada test, duración, capturas en fallos, metadata del proyecto
- **Se genera:** Automáticamente en cada ejecución de pytest

### Logs
- **Ubicación:** `reports/logs/log_YYYY-MM-DD_HH-MM-SS.log`
- **Contiene:** Cada acción de los tests con timestamp
- **Útil para:** Depuración post-ejecución

### Capturas de Pantalla
- **Ubicación:** `reports/screenshots/`
- **Se genera:** Automáticamente solo cuando un test de UI falla
- **Formato:** `nombre_del_test_YYYY-MM-DD_HH-MM-SS.png`

## CI/CD con GitHub Actions

El proyecto incluye un pipeline automático que se ejecuta en cada push o pull request a `main`. El pipeline:

1. Instala Python y dependencias
2. Instala Chrome en el runner
3. Ejecuta los tests de API
4. Ejecuta los tests de UI en modo headless
5. Ejecuta los escenarios BDD con Behave
6. Sube los reportes como artefactos descargables (disponibles 90 días)

El estado del pipeline se muestra en el badge al inicio de este README.

## Notas Importantes

- Los tests de UI requieren **Chrome instalado** en el sistema
- El proyecto usa **encoding UTF-8** para soportar caracteres especiales
- Las rutas se construyen con `pathlib` para compatibilidad multiplataforma (Windows/Linux/Mac)
- El fixture `driver_logged` busca automáticamente el primer usuario válido del CSV
- Los reportes y logs se crean automáticamente al correr pytest
- Las capturas de pantalla se integran automáticamente al reporte HTML