import telebot
from dotenv import load_dotenv
import os
import datetime
import requests
from bs4 import BeautifulSoup

load_dotenv()
TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")
bot = telebot.TeleBot(TOKEN)

def is_PS26_2():
    """Verifica se há processo seletivo extra para 2026.2 no site da UFRPE"""
    try:
        response = requests.get("http://selecao.ufrpe.br", timeout=15)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        titles = soup.find_all('h4')
        for title in titles:
            if 'INGRESSO EXTRA PARA 2026.2' in title.get_text(strip=True):
                return True
        return False
    except Exception as e:
        print(f"Erro ao acessar o site: {e}")
        return False

def send_result(found):
    if found:
        text = f'PS extra 2026 encontrado! {datetime.datetime.today().strftime("%d/%m/%Y")}'
    else:
        text = f'Não há PS aberto. {datetime.datetime.today().strftime("%d/%m/%Y")}'
    bot.send_message(CHAT_ID, text)

def main():
    send_result(is_PS26_2())


main()
