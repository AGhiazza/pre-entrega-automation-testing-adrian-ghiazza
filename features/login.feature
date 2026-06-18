Feature: Login en SauceDemo

    Scenario: Login exitoso
        Given el usuario está en la página de login
        When ingresa usuario "standard_user" y contraseña "secret_sauce"
        Then debería ver la página de inventario

    Scenario: Login fallido (credenciales incorrectas)
        Given el usuario está en la página de login
        When ingresa usuario "standardt_user" y contraseña "secret_sauce"
        Then debería ver el error "Username and password do not match any user in this service"

    Scenario: Login fallido (campos vacios)
        Given el usuario está en la página de login
        When ingresa usuario "" y contraseña ""
        Then debería ver el error "Username is required"

    Scenario: Login fallido (usuario vacio)
        Given el usuario está en la página de login
        When ingresa usuario "" y contraseña "secret_sauce"
        Then debería ver el error "Username is required"

    Scenario: Login fallido (contraseña vacia)
        Given el usuario está en la página de login
        When ingresa usuario "standard_user" y contraseña ""
        Then debería ver el error "Password is required"

