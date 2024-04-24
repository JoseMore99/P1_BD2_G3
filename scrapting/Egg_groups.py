# imports
import requests
from bs4 import BeautifulSoup
import csv

# web scrapping page url
url='https://pokemondb.net/egg-group/grass'

# HTTP request
response =requests.get(url)

# BeautifulSoup object
soup= BeautifulSoup(response.text,'html.parser')

# CSV FILE
csv_file=open('./otros/eggGroups.csv','w',newline='',encoding='utf-8')
csv_writter=csv.writer(csv_file)
csv_writter.writerow(['tipo'])

# find all pokemons
div=soup.find('div',class_="grid-col span-md-4")
panel=div.find_all('ul',class_=None)
print(panel)
tipos=panel[0].find_all('a')
# Travel around rows
for tipo in tipos:
  #obtain all columns of each row
  cells=tipo.text
  
  print("Name:",cells)
  # Write pokemon data on csv file
  csv_writter.writerow([cells])
    