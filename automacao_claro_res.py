from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

# Inicia o navegador Chrome
navegador = webdriver.Chrome()

try:
    # Abre o site da Claro
    navegador.get("https://www.claro.com.br/")
    print("Entrando no site...")
    sleep(5)
    
    # Clica no botão "Minha Claro"
    navegador.find_element(By.XPATH, '//*[@id="cms-Header"]/div[2]/div/nav/div[2]/ul/li[2]/div[1]/button').click()
    print("Clicando em Minha Claro...")
    sleep(5)
    
    # Clica em "Minha Claro Residencial"
    navegador.find_element(By.XPATH, '//*[@id="cms-Header"]/div[2]/div/nav/div[2]/ul/li[2]/div[2]/ul/li/div/ul/li[2]/a').click()
    print("Clicando em Minha Claro Residencial...")
    sleep(5)
    
    # Clica em "Entrar"
    navegador.find_element(By.XPATH, '//*[@id="public-area"]/header/div[2]/nav/div[2]/ul/li/div/a').click()
    print("Clicando em Entrar...")
    sleep(5)

    # Preenche o login
    navegador.find_element(By.XPATH, '//*[@id="mdn-MainContent"]').send_keys('12345678910')
    navegador.find_element(By.XPATH, '//*[@id="FormLogin"]/div[3]/button').click()
    sleep(3)
    print("Preenchendo o login...")
    
    # Preenche a senha

    navegador.find_element(By.XPATH, '//*[@id="password"]').send_keys('Senha-123')
    navegador.find_element(By.XPATH, '//*[@id="FormLogin"]/div[3]/button').click()
    sleep(20)
    print("Preenchendo a senha...")

    # Clicar para pegar a segunda via da conta 

    navegador.find_element(By.XPATH, '//*[@id="mfe-dashboard"]/section/div[2]/div[2]/div[3]/a[2]').click()
    sleep(10)
    print("Clicando em acessar a segunda via da fatura...") 

    # Clicar para pegar a segunda via da conta 

    navegador.find_element(By.XPATH, '//*[@id="interactive-invoice"]/section/div/div[2]/div[3]/div/div/div[1]/div[2]/div[2]/div/div[2]/a[1]').click()
    sleep(10)
    print("Clicando em segunda via da fatura...")

    # Clicando em imprimir a fatura

    navegador.find_element(By.XPATH('//*[@id="interactive-invoice"]/section/div/div[2]/div[1]/button[3]')).click()
    sleep(5)
    print('Imprimindo a fatura...')














except Exception as e:
    print(f"Ocorreu um erro: {e}")

finally:
    # Fecha o navegador
    navegador.quit()


