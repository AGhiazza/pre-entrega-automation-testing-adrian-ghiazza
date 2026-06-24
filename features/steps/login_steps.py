from pages.LoginPage import LoginPage
from behave import given, when, then
from utils.config import INVENTORY_PATH

@given("el usuario está en la página de login")
def step_abrir_login(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.abrir_pagina()

@when("ingresa usuario '{usuario}' y contraseña '{contrasena}'")
def step_ingresar_credenciales(context,usuario,contrasena):
    if usuario == "VACIO": #Si el valor es VACIO, lo cambia por "" para que no falle al leer la información
        usuario = ""
    if contrasena == "VACIO":
        contrasena = ""
    context.login_page.ingresar_usuario(usuario)
    context.login_page.ingresar_contrasena(contrasena)

@when("hace click en boton login")
def step_click_login(context):
    context.login_page.click_login()

@then("debería ver la página de inventario")
def step_validar_login_exitoso(context):
    assert INVENTORY_PATH in context.driver.current_url, "No se visualiza la pagina del inventario"

@then("debería ver el error '{mensaje}'")
def step_validar_error_login(context, mensaje):
    error = context.login_page.obtener_mensaje_error()
    assert mensaje in error, f"Mensaje de error esperado: {mensaje} | Recibido: {error}"