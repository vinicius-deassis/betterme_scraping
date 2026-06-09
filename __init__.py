from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://selecao.ufrpe.br")
driver.implicitly_wait(10)
titles = driver.find_elements(By.TAG_NAME,'h4')

def is_PS26_2():
    for title in titles:
        #print(title.text)
        if 'INGRESSO EXTRA PARA 2026.1' in title.text:
            return True

if is_PS26_2():
    print("PS extra 2026 encontrado!")
else:
    print("Não há PS extra aberto.")