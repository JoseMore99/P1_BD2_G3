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
csv_file=open('./pokemons/pokemon_desc.csv','w',newline='',encoding='utf-8')
csv_writter=csv.writer(csv_file)
csv_writter.writerow(['pokedex_id','game','description '])

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
    info_table=soup.find_all('table',class_='vitals-table')
    info=info_table[4].find_all('th')
    game=[a.text for a in info[0].find_all('span')]
    if len(game)>0:
      textos = info_table[4].find_all('td')
    else:
      info=info_table[8].find_all('th')
      game=[a.text for a in info[0].find_all('span')]
      if len(game)>0:
        textos = info_table[8].find_all('td')
      else:
        info=info_table[12].find_all('th')
        game=[a.text for a in info[0].find_all('span')]
        if len(game)>0:
          textos = info_table[12].find_all('td')
        else:
          info=info_table[16].find_all('th')
          game=[a.text for a in info[0].find_all('span')]
          if len(game)>0:
            textos = info_table[16].find_all('td')
          else:
            info=info_table[20].find_all('th')
            game=[a.text for a in info[0].find_all('span')]
            if len(game)>0:
              textos = info_table[20].find_all('td')
            else:
              info=info_table[24].find_all('th')
              game=[a.text for a in info[0].find_all('span')]
              if len(game)>0:
                textos = info_table[24].find_all('td')
              else:
                info=info_table[28].find_all('th')
                textos = info_table[28].find_all('td')
    for i in range(len(info)):
      game=[a.text for a in info[i].find_all('span')]
      All_game = game
      texto =textos[i].text
      csv_writter.writerow([pokedex_number,All_game,texto])


    
    