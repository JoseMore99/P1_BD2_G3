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
csv_file=open('./pokemons/Breeding.csv','w',newline='',encoding='utf-8')
csv_writter=csv.writer(csv_file)
csv_writter.writerow(['pokedex_id','Egg_groups','gender_male ','gender_female ','egg_cycles'])

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
        
    url='https://pokemondb.net'+href

    # HTTP request
    response =requests.get(url)
    # BeautifulSoup object
    soup= BeautifulSoup(response.text,'html.parser')
    div=soup.find_all('div',class_='grid-col span-md-6 span-lg-12')
    info_table=div[1].find('table',class_='vitals-table')
    info=info_table.find_all('tr')
    groups=[a.text for a in info[0].find_all('a')]
    Egg_groups = groups
    texto = info[1].find('td').text.replace("\n","").replace("\"","").split(",")
    if info[1].find('td').text!="Genderless":
      gender_male=texto[0]
      gender_female =texto[1]
    else:
      gender_male="Genderless"
      gender_female ="Genderless"
    egg_cycles =info[2].find('td').text.replace("\n","")
    # Write pokemon data on csv file
    csv_writter.writerow([
    pokedex_number,Egg_groups,gender_male,gender_female,egg_cycles])
    