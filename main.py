from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import telebot
from dotenv import load_dotenv
import os
import datetime

load_dotenv()
TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")
bot = telebot.TeleBot(TOKEN)

def is_PS26_2():
    # Chrome settings on selenium
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome(options=chrome_options)
    driver.get("http://selecao.ufrpe.br")
    driver.implicitly_wait(10)
    titles = driver.find_elements(By.TAG_NAME, 'h4')
    for title in titles:
        #print(title.text)
        if 'INGRESSO EXTRA PARA 2026.2' in title.text:
            driver.quit()
            return True
    driver.quit()

def send_result(found):
    if found:
        text = f'PS extra 2026 encontrado! {datetime.datetime.today().strftime('%d/%m/%Y')}'
    else:
        text = f'Não há PS aberto. {datetime.datetime.today().strftime('%d/%m/%Y')}'
    bot.send_message(CHAT_ID, text)

def main():
    send_result(is_PS26_2())


main()