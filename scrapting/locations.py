# imports
import requests
from bs4 import BeautifulSoup
import csv

# web scrapping page url
url='https://pokemondb.net/location'

# HTTP request
response =requests.get(url)

# BeautifulSoup object
soup= BeautifulSoup(response.text,'html.parser')

# CSV FILE
csv_file=open('./otros/locations.csv','w',newline='',encoding='utf-8')
csv_writter=csv.writer(csv_file)
csv_writter.writerow(['name','gen_game'])

# find all pokemons

locations_table=soup.find_all('div',class_='sv-tabs-panel')
count=1
for location in locations_table:
  #obtain all columns of each row
    lugares = location.find_all('a')
    
    for i in lugares:
        lugar=i.text
        csv_writter.writerow([lugar,count])
    lugares = location.find_all('span')
    
    for i in lugares:
        lugar=i.text
        csv_writter.writerow([lugar,count])
    count+=1
    