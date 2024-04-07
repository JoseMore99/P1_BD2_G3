# imports
import requests
from bs4 import BeautifulSoup
import csv

# web scrapping page url
url='https://bulbapedia.bulbagarden.net/wiki/Mega_Evolution'

# HTTP request
response =requests.get(url)

# BeautifulSoup object
soup= BeautifulSoup(response.text,'html.parser')

# CSV FILE
csv_file=open('./pokemons/megas.csv','w',newline='',encoding='utf-8')
csv_writter=csv.writer(csv_file)
csv_writter.writerow(['Evolving_from','Evolving_to','item','description'])

# find all pokemons

pokeevos_table=soup.find_all('table',class_='roundy')
count=1
for pokeevo in pokeevos_table:
  #obtain all columns of each row
    filas = pokeevo.find_all('tr')
    Anterior=""
    Anteriorev=""
    for i in filas:
        lst=i.find_all("td")
        if len(lst)>0:
          try:
            poke =lst[1].text.replace("\n","")
            pokev =f'{lst[1].text}(Mega {lst[1].text})'.replace("\n","")
            try:
              item =lst[8].text.replace("\n","")
              anterior=poke
              Anteriorev=pokev
              csv_writter.writerow([poke,pokev,item,'MegaEvolution'])
            except:
              item =lst[3].text.replace("\n","")
              csv_writter.writerow([anterior,Anteriorev,item,'MegaEvolution'])
          except:
             pass