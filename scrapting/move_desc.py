# imports
import requests
from bs4 import BeautifulSoup
import csv

# web scrapping page url
csv_file=open(f'./movimientos/moviminetos_desc.csv','w',newline='',encoding='utf-8')
csv_writter=csv.writer(csv_file)
csv_writter.writerow(['name','game','description'])
url='https://pokemondb.net/move/all'

# HTTP request
response =requests.get(url)

# BeautifulSoup object
soup= BeautifulSoup(response.text,'html.parser')


movimientos_table=soup.find('table',class_='data-table sticky-header block-wide')
movimientos=movimientos_table.find_all('tr')
# Travel around rows
for movimiento in movimientos:
  cells=movimiento.find_all('td')
  if cells:
    name=cells[0].find('a',class_='ent-name').text
    href=cells[0].find('a',class_='ent-name')["href"]
        
    url='https://pokemondb.net'+href

    # HTTP request
    response =requests.get(url)
    # BeautifulSoup object
    soup= BeautifulSoup(response.text,'html.parser')
    info_div=soup.find_all('div',class_='grid-col span-md-12 span-lg-8')
    if len(info_div)>0:
      info_table=info_div[0].find('table',class_='vitals-table')
      if info_table:
        info=info_table.find_all('th')
        textos = info_table.find_all('td')

        for i in range(len(info)):
          game=[a.text for a in info[i].find_all('span')]
          All_game = game
          texto =textos[i].text
          csv_writter.writerow([name,All_game,texto])
        