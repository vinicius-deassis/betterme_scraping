import requests
# Remove os avisos chatos de "InsecureRequestWarning" no terminal
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = 'https://selecao.ufrpe.br/'

# O 'verify=False' ignora o erro de certificado SSL
resposta = requests.get(url, verify=False)

if 'INGRESSO EXTRA PARA 2026.2' in resposta.text:
    print("PS extra 2026 encontrado!")
else:
    print("Não há PS extra aberto.")

