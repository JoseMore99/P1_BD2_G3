# imports
import requests
from bs4 import BeautifulSoup
import csv

# web scrapping page url
url='https://pokemondb.net/ability'

# HTTP request
response =requests.get(url)

# BeautifulSoup object
soup= BeautifulSoup(response.text,'html.parser')
lista_abil=[]
lista_url=[]
# CSV FILE

csv_file=open('./otros/ability_all.csv','w',newline='',encoding='utf-8')
csv_writter=csv.writer(csv_file)
csv_writter.writerow(['ability','game','Description'])

# find all pokemons
pokemons_table=soup.find('table',class_='data-table sticky-header block-wide')
pokemons=pokemons_table.find_all('tr')
# Travel around rows
for pokemon in pokemons:
  #obtain all columns of each row
  cells=pokemon.find_all('td')
  if cells:
    link=cells[0].find('a',class_='ent-name')["href"]
    name=cells[0].find('a',class_='ent-name').text
        
    url='https://pokemondb.net'+link

    response =requests.get(url)
    # BeautifulSoup object
    soup= BeautifulSoup(response.text,'html.parser')
    print(name)
    try:
      info_table=soup.find('table',class_='vitals-table')
      filas = info_table.find_all('tr')
      for i in filas:
        info=i.find_all('th')
        game=[a.text for a in info[0].find_all('span')]
        textos = i.find('td')
        descr=textos.text
        csv_writter.writerow([name,game,descr])
    except:
      info_table=soup.find('div',class_='grid-col span-md-12 span-lg-6')
      textos = info_table.find('p').text
      csv_writter.writerow([name,['Scarlet', 'Violet'],textos])
      