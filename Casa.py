import requests
from bs4 import BeautifulSoup

#pegando o dolar
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'}
pagina = requests.get('https://www.google.com/search?q=dolar&oq=dolar&aqs=edge.0.69i59j69i57j69i59l2.687j0j1&sourceid=chrome&ie=UTF-8',headers=headers)
soup = BeautifulSoup(pagina.content, 'html.parser')
atributos = {'class':'DFlfde SwHCTb'}
dolar = soup.find_all('span', attrs=atributos)[0]


#pegando euro
headerse = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'}
paginae = requests.get('https://www.google.com/search?q=euro&oq=euro&aqs=edge.0.69i59j0i131i433i512j0i433i512l2j0i131i433i512l3j0i67i131i433.2208j0j9&sourceid=chrome&ie=UTF-8',headers=headerse)
soupe = BeautifulSoup(paginae.content, 'html.parser')
atributose = {'class':'DFlfde SwHCTb'}
euro = soupe.find_all('span', attrs=atributos)[0]

#pegando bitcoin
headersb = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'}
paginab = requests.get('https://www.google.com/search?q=bitcoin&oq=bit&aqs=edge.0.69i59j69i57j0i131i433i512l3j0i433i512j0i131i433i512l3.1057j0j1&sourceid=chrome&ie=UTF-8', headers=headersb)
soupb = BeautifulSoup(paginab.content, 'html.parser')
atributosb = {'class':'pclqee'}
bitcoin = soupb.find_all('span', attrs=atributosb)[0]

print(f'{"Casa de Câmbio":=^30}')
print(f'Dolar:$[{dolar.text}]')
print(f'Euro:€[{euro.text}]')
print(f'Bitcoin:₿[{bitcoin.get_text()}]')
print(30 * '=')






