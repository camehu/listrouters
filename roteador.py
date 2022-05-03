import requests
from bs4 import BeautifulSoup

for i in range ( 49, 1969, 48 ):
    site = requests.get (f'https://informatica.mercadolivre.com.br/conectividade-e-redes-roteadores/roteadores_Desde_{i}_NoIndex_True' )
    soup = BeautifulSoup(site.content, 'html.parser' )
    paginas = []
    paginas = soup.find_all( 'h2', attrs={'class' : 'ui-search-item__title ui-search-item__group__element'} )














