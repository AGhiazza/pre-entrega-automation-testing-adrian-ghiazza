Feature: Login en SauceDemo

    Background:
        Given el usuario está en la página de login

    Scenario: Login exitoso
        When ingresa usuario 'standard_user' y contraseña 'secret_sauce'
        And hace click en boton login
        Then debería ver la página de inventario

    Scenario Outline: Login invalido
        When ingresa usuario '<usuario>' y contraseña '<contrasena>'
        And hace click en boton login
        Then debería ver el error '<mensaje>'

        Examples:
        | usuario       | contrasena   | mensaje                                                    |
        | standardt_user| secret_sauce | Username and password do not match any user in this service|
        | standard_user| secretd_sauce | Username and password do not match any user in this service|
        | VACIO | VACIO | Username is required                                       |
        | VACIO | secret_sauce | Username is required                                       |
        | standard_user | VACIO | Password is required|