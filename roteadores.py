import json

import requests
from bs4 import BeautifulSoup

def Roteadores():
    for i in range(49, 100, 48):
        site = requests.get(f'https://informatica.mercadolivre.com.br/conectividade-e-redes-roteadores/roteadores_Desde_{i}_NoIndex_True')
        soup = BeautifulSoup(site.content, 'html.parser')
        paginas = soup.find_all('h2', class_='ui-search-item__title ui-search-item__group__element')

    return paginas











