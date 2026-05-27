# Selectors - Proyecto TalentoTech
https://www.saucedemo.com

---

## Login Page

| Elemento | Tipo | Selector | DOM | Descripción |
|----------|------|----------|-----|-------------|
| Input Usuario | ID | `#user-name` | `id="user-name"` | Campo de nombre de usuario |
| Input Password | ID | `#password` | `id="password"` | Campo de contraseña |
| Botón Login | ID | `#login-button` | `id="login-button"` | Botón de submit del formulario |
| Contenedor error | Class | `.error-message-container h3` | `class="error-message-container"` | Contenedor del mensaje de error |
| Mensaje de error | CSS | `[data-test="error"]` | `data-test="error"` | Texto del mensaje de error |

---

## Header

| Elemento | Tipo | Selector | DOM | Descripción |
|----------|------|----------|-----|-------------|
| Botón hamburguesa | ID | `#react-burger-menu-btn` | `id="react-burger-menu-btn"` | Abre el menú lateral |
| Botón About | ID | `#about_sidebar_link` | `id="about_sidebar_link"` | Lleva a página externa de Sauce Labs |
| Botón Logout | ID | `#logout_sidebar_link` | `id="logout_sidebar_link"` | Cierra la sesión |
| Botón Reset | ID | `#reset_sidebar_link` | `id="reset_sidebar_link"` | Resetea el estado de la página |
| Logo / Título | Class | `.app_logo` | `class="app_logo"` | Texto "Swag Labs" en el header |
| Carrito | Class | `.shopping_cart_link` | `class="shopping_cart_link"` | Link al carrito de compras |
| Badge carrito | Class | `.shopping_cart_badge` | `class="shopping_cart_badge"` | Indicador de cantidad de productos en el carrito |
| Ordenar | Class | `.product_sort_container` | `class="product_sort_container"` | Contenedor del filtro de ordenamiento |

---

## Inventory Page

| Elemento | Tipo | Selector | DOM | Descripción |
|----------|------|----------|-----|-------------|
| Lista de productos | Class | `.inventory_list` | `class="inventory_list"` | Contenedor de todas las tarjetas de productos |
| Tarjeta de producto | Class | `.inventory_item` | `class="inventory_item"` | Tarjeta individual de producto |
| Nombre | Class | `.inventory_item_name` | `class="inventory_item_name"` | Nombre del producto en la tarjeta |
| Descripción | Class | `.inventory_item_desc` | `class="inventory_item_desc"` | Descripción del producto en la tarjeta |
| Precio | Class | `.inventory_item_price` | `class="inventory_item_price"` | Precio del producto en la tarjeta |
| Imagen | Class | `.inventory_item_img` | `class="inventory_item_img"` | Imagen del producto en la tarjeta |
| Botón Agregar | ID | `#add-to-cart-sauce-labs-backpack` | `id="add-to-cart-sauce-labs-backpack"` | Botón de añadir producto al carrito |

---

## Item Detail

| Elemento | Tipo | Selector | DOM | Descripción |
|----------|------|----------|-----|-------------|
| Nombre | Class | `.inventory_item_name` | `class="inventory_item_name"` | Nombre del producto |
| Descripción | Class | `.inventory_item_desc` | `class="inventory_item_desc"` | Descripción del producto |
| Precio | Class | `.inventory_item_price` | `class="inventory_item_price"` | Precio del producto |
| Imagen | Class | `.inventory_item_img` | `class="inventory_item_img"` | Imagen del producto |
| Botón Agregar | ID | `#add-to-cart-sauce-labs-backpack` | `id="add-to-cart-sauce-labs-backpack"` | Botón de añadir producto al carrito |

---

## Cart

| Elemento | Tipo | Selector | DOM | Descripción |
|----------|------|----------|-----|-------------|
| Título | Class | `.title` | `class="title"` | Título de la página "Your Cart" |
| Cantidad | Class | `.cart_quantity` | `class="cart_quantity"` | Cantidad del mismo producto en el carrito |
| Nombre | Class | `.inventory_item_name` | `class="inventory_item_name"` | Nombre del producto en el carrito |
| Descripción | Class | `.inventory_item_desc` | `class="inventory_item_desc"` | Descripción del producto en el carrito |
| Precio | Class | `.inventory_item_price` | `class="inventory_item_price"` | Precio del producto en el carrito |
| Imagen | Class | `.inventory_item_img` | `class="inventory_item_img"` | Imagen del producto en el carrito |
| Botón Remove | ID | `#remove-sauce-labs-backpack` | `id="remove-sauce-labs-backpack"` | Botón para eliminar producto del carrito |
| Botón Continue Shopping | ID | `#continue-shopping` | `id="continue-shopping"` | Vuelve a la página de inventario |
| Botón Checkout | ID | `#checkout` | `id="checkout"` | Avanza al proceso de pago |
