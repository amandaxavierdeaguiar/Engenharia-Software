""" 
Crie um código em Pythonque teste se o site do IEFP está acessível a partir do seu computador.
"""
import requests

url = 'https://iefponline.iefp.pt/IEFP/index2.jsp'

if requests.get(url).status_code == 200:
    print("O servidor está disponível.")
else:
    print("O servidor está indisponível.")

"""
Para ver todo o código html do site.
url = 'https://iefponline.iefp.pt/IEFP/index2.jsp'
res = requests.get(url)
print(res.text)
"""