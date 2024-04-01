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
csv_file=open('./otros/items_desc.csv','w',newline='',encoding='utf-8')
csv_writter=csv.writer(csv_file)
csv_writter.writerow(['name','game','description'])

# find all pokemons
items_table=soup.find('table',class_='data-table block-wide')
items=items_table.find_all('tr')
# Travel around rows
for item in items:
  #obtain all columns of each row
  cells=item.find_all('td')
  if cells:
    name=cells[0].find('a',class_='ent-name').text
    href=cells[0].find('a',class_='ent-name')["href"]
        
    url='https://pokemondb.net'+href

    # HTTP request
    response =requests.get(url)
    # BeautifulSoup object
    soup= BeautifulSoup(response.text,'html.parser')
    info_div=soup.find_all('div',class_='resp-scroll')
    if len(info_div)>0:
      info_table=info_div[0].find('table',class_='vitals-table')
      info=info_table.find_all('th')
      textos = info_table.find_all('td')

      for i in range(len(info)):
        game=[a.text for a in info[i].find_all('span')]
        All_game = game
        texto =textos[i].text
        csv_writter.writerow([name,All_game,texto])