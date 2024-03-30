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
csv_file=open('./pokemons/Training.csv','w',newline='',encoding='utf-8')
csv_writter=csv.writer(csv_file)
csv_writter.writerow(['pokedex_id','EV_yield','catch_rate ','base_friendship','base_exp','growth_rate '])

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
    info_table=div[0].find('table',class_='vitals-table')
    info=info_table.find_all('tr')
    
    EV_yield=info[0].find('td').text.replace("\n","")
    catch_rate =info[1].find('td').text.replace("\n","")
    base_friendship =info[2].find('td').text.replace("\n","")
    base_exp =info[3].find('td').text.replace("\n","")
    growth_rate =info[4].find('td').text.replace("\n","")
    # Write pokemon data on csv file
    csv_writter.writerow([
    pokedex_number,EV_yield,catch_rate,base_friendship,base_exp,growth_rate])
    