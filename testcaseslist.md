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