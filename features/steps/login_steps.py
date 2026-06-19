from pages.LoginPage import LoginPage
from behave import given, when, then

@given("el usuario está en la página de login")
def step_abrir_login(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.abrir_pagina()

@when("ingresa usuario '{usuario}' y contraseña '{contrasena}'")
def step_ingresar_credenciales(context,usuario,contrasena):
    if usuario == "VACIO":
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
    assert "/inventory.html" in context.driver.current_url, "No se visualiza la pagina del inventario"

@then("debería ver el error '{mensaje}'")
def step_validar_error_login(context, mensaje):
    error = context.login_page.mensaje_error()
    assert mensaje in error, f"Mensaje de error esperado: {mensaje} | Recibido: {error}"