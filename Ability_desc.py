# imports
import requests
from bs4 import BeautifulSoup
import csv

# web scrapping page url
url='https://pokemondb.net/pokedex/all'

# HTTP request
response =requests.get(url)

# BeautifulSoup object
soup= BeautifulSoup(response.text,'html.parser')
lista_abil=[]
lista_url=[]
# CSV FILE

# find all pokemons
pokemons_table=soup.find('table',class_='data-table sticky-header block-wide')
pokemons=pokemons_table.find_all('tr')
# Travel around rows
for pokemon in pokemons:
  #obtain all columns of each row
  cells=pokemon.find_all('td')
  if cells:
    pokedex_number=cells[0].find('span',class_='infocard-cell-data').text
    name=cells[1].find('a',class_='ent-name')["href"]
        
    url='https://pokemondb.net'+name

    # HTTP request
    response =requests.get(url)
    # BeautifulSoup object
    soup= BeautifulSoup(response.text,'html.parser')
    info_table=soup.find('table',class_='vitals-table')
    info=info_table.find_all('tr')
    
    abilitys =info[5].find('td')
    # Write pokemon data on csv file
    for i in abilitys.find_all('a'):
      if i.text not in lista_abil:
        lista_abil.append(i.text)
        lista_url.append(i["href"])

csv_file=open('./otros/ability_desc.csv','w',newline='',encoding='utf-8')
csv_writter=csv.writer(csv_file)
csv_writter.writerow(['ability','language','Deescription'])

print(lista_abil)
for j in range(len(lista_url)):

  url='https://pokemondb.net'+lista_url[j]
  # HTTP request
  response =requests.get(url)
  # BeautifulSoup object
  soup= BeautifulSoup(response.text,'html.parser')
  info_table=soup.find('table',class_='vitals-table')
  filas = info_table.find_all('tr')
  for i in filas:
    info=i.find_all('th')
    game=[a.text for a in info[0].find_all('span')]
    textos = i.find('td')
    habilidad=lista_abil[j]
    descr=textos.text
    csv_writter.writerow([habilidad,game,descr])
      