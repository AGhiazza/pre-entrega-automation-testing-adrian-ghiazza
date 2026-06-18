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