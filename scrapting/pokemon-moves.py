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

# CSV FILE
csv_file=open('./pokemons/pokemon_move_bytm.csv','w',newline='',encoding='utf-8')
csv_writter=csv.writer(csv_file)
csv_writter.writerow(['pokedex_id','move_name'])
atacantes=[]
# find all pokemons
pokemons_table=soup.find('table',class_='data-table sticky-header block-wide')
pokemons=pokemons_table.find_all('tr')
# Travel around rows
for pokemon in pokemons:
  #obtain all columns of each row
  cells=pokemon.find_all('td')
  if cells:
    pokedex_number=cells[0].find('span',class_='infocard-cell-data').text
    href=cells[1].find('a',class_='ent-name')["href"]
    if pokedex_number in atacantes:
      continue
    url='https://pokemondb.net'+href

    # HTTP request
    response =requests.get(url)
    # BeautifulSoup object
    soup= BeautifulSoup(response.text,'html.parser')
    info_table=soup.find_all('table',class_='data-table')
    #print(info_table[0])
    for k in range(len(info_table)):
      info=info_table[k].find_all('tr')
      info2=info_table[k].find('th')
      if info2 and info2.text=="TM":
        for i in info[1:]:
          datos = i.find_all('td')
          mov =datos[1].find('a').text
          csv_writter.writerow([pokedex_number,mov])
        break


    
    