from selenium import webdriver
from commands.commands import *
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from datetime import datetime

# Configurações para Chrome em modo headless
chrome_options = Options()
chrome_options.add_argument("--headless")

driver = webdriver.Chrome(options=chrome_options)#
driver.implicitly_wait(5)
driver.maximize_window()

def test_loginSaucedemo():
    time = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
    screenshot_filename = f"screenshot_{time}.png"
    driver.get("https://www.saucedemo.com")
    print('Pagina da Saucedemo Acessada com Sucesso!')
    screenshot_path_01 = fr"C:\Estudos\udemy\Selenium_Modelo_Test\test\04_login_Saucedemo\report\{screenshot_filename}_01.png"
    driver.save_screenshot(screenshot_path_01)
    driver.find_element(By.ID, "user-name").send_keys(username)
    print('Usuário Inserido  com Sucesso!')
    driver.find_element(By.ID, "password").send_keys(password)
    print('Senha Inserida com Sucesso!')
    screenshot_path_02 = fr"C:\Estudos\udemy\Selenium_Modelo_Test\test\04_login_Saucedemo\report\{screenshot_filename}_02.png"
    driver.save_screenshot(screenshot_path_02)
    driver.find_element(By.ID, "login-button").click()
    print('Botão de Entrar clicado com Sucesso!')
    assert driver.find_element(By.XPATH, "//span[@class='title']").is_displayed()
    print('Login Efetuado com Sucesso! Componente confirmado na tela Inicial!')
    screenshot_path_03 = fr"C:\Estudos\udemy\Selenium_Modelo_Test\test\04_login_Saucedemo\report\{screenshot_filename}_03.png"
    driver.save_screenshot(screenshot_path_03)
    driver.quit()