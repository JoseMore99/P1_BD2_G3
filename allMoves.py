# imports
import requests
from bs4 import BeautifulSoup
import csv

gen=9
# web scrapping page url
url='https://pokemondb.net/move/generation/'+str(gen)

# HTTP request
response =requests.get(url)

# BeautifulSoup object
soup= BeautifulSoup(response.text,'html.parser')

csv_file=open(f'./movimientos/moviminetos{gen}.csv','w',newline='',encoding='utf-8')
csv_writter=csv.writer(csv_file)
csv_writter.writerow(['name','types','power','Category','acc','pp','efect'])

movimientos_table=soup.find('table',class_='data-table sticky-header block-wide')
movimientos=movimientos_table.find_all('tr')
# Travel around rows
for movimiento in movimientos:
  cells=movimiento.find_all('td')
  if cells:
    name=cells[0].find('a',class_='ent-name').text
    if cells[1].find('a'):
        type=cells[1].find('a').text
    else:
        type=""
    Category=cells[2]["data-filter-value"]
    power=cells[3].text
    Acc=cells[4].text
    if Acc =="∞":
       Acc=-1
    
    pp=cells[5].text
    efect=cells[6].text
    csv_writter.writerow([
      name,type,power,Category,Acc,pp,efect
    ])
    