# imports
import requests
from bs4 import BeautifulSoup
import csv

# web scrapping page url
url='https://pokemondb.net/item/all'

# HTTP request
response =requests.get(url)

# BeautifulSoup object
soup= BeautifulSoup(response.text,'html.parser')

# CSV FILE
csv_file=open('./otros/items.csv','w',newline='',encoding='utf-8')
csv_writter=csv.writer(csv_file)
csv_writter.writerow(['name','effect','cathegory'])

# find all pokemons
items_table=soup.find('table',class_='data-table block-wide')
items=items_table.find_all('tr')
# Travel around rows
for item in items:
  #obtain all columns of each row
  cells=item.find_all('td')
  if cells:
    name=cells[0].find('a',class_='ent-name').text
    cathegory=cells[1].text
    effect=cells[2].text

    # Print item data
    #print("Pokedex number:",pokedex_number)
    #print("Name:",name)
    # Write item data on csv file
    csv_writter.writerow([
      name,effect,cathegory
    ])
    