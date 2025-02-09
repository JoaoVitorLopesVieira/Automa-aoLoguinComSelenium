from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

# Configura o serviço do ChromeDriver
service = Service(ChromeDriverManager().install())
# Inicializa o navegador
navegador = webdriver.Chrome(service=service)
# Abre a página
navegador.get("https://joaovitorlopesvieira.github.io/PaginaDeLoguinDaPutCode/")
time.sleep(2)
navegador.find_element('xpath', '//*[@id="formulario"]/div/input[1]').send_keys('Joao Vitor Lopes Vieira')
time.sleep(2)
navegador.find_element('xpath', '//*[@id="formulario"]/div/input[2]').send_keys('Arinos')
time.sleep(2)
navegador.find_element('xpath', '//*[@id="formulario"]/div/input[3]').send_keys('Minas Gerais')
time.sleep(2)
navegador.find_element('xpath', '//*[@id="formulario"]/div/input[4]').send_keys('Brasil')
time.sleep(2)
navegador.find_element('xpath', '//*[@id="download"]]').click
time.sleep(2)
# Aguarda um tempo antes de fechar o navegador
time.sleep(10)  # Espera 10 segundos

# Fecha o navegador
navegador.quit()