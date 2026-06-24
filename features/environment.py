from selenium import webdriver

def before_scenario(context, scenario):
    # Se ejecuta antes de cada escenario
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")

    context.driver = webdriver.Chrome(options=options)

def after_scenario(context, scenario):
    # Se ejecuta después de cada escenario
    context.driver.quit()