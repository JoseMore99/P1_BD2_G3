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
csv_file=open('./pokemons/pokemon_indi.csv','w',newline='',encoding='utf-8')
csv_writter=csv.writer(csv_file)
csv_writter.writerow(['pokedex_id','name','especie','height','weight','nature'])

# find all pokemons
pokemons_table=soup.find('table',class_='data-table sticky-header block-wide')
pokemons=pokemons_table.find_all('tr')
# Travel around rows
for pokemon in pokemons:
  #obtain all columns of each row
  cells=pokemon.find_all('td')
  if cells:
    pokedex_number=cells[0].find('span',class_='infocard-cell-data').text
    url=cells[1].find('a',class_='ent-name')["href"]
    name= cells[1].find('a',class_='ent-name').text
    subname =cells[1].find('small')
    if subname:
      name +=f'({subname.text})'
    url='https://pokemondb.net'+url

    # HTTP request
    response =requests.get(url)
    # BeautifulSoup object
    soup= BeautifulSoup(response.text,'html.parser')
    info_table=soup.find('table',class_='vitals-table')
    info=info_table.find_all('tr')
    
    numero_nacional=info[0].find('strong').text
    especie=info[2].find('td').text
    height =info[3].find('td').text
    weight =info[4].find('td').text
    # Write pokemon data on csv file
    csv_writter.writerow([
    pokedex_number,name,especie,height,weight])
    