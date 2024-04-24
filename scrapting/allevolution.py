# imports
import requests
from bs4 import BeautifulSoup
import csv

# web scrapping page url
# CSV FILE
csv_file=open('./evoluciones/evos3.csv','w',newline='',encoding='utf-8')
csv_writter=csv.writer(csv_file)
csv_writter.writerow(['Evolving_from','Evolving_to','level','item','description','type'])
enlistados=[]


url='https://pokemondb.net/evolution/level'

# HTTP request
response =requests.get(url)

# BeautifulSoup object
soup= BeautifulSoup(response.text,'html.parser')


# find all pokemons
items_table=soup.find('table',class_='data-table')
items=items_table.find_all('tr')
# Travel around rows
for item in items:
  #obtain all columns of each row
  cells=item.find_all('td')
  if cells:
    actual=cells[0].find('a',class_='ent-name').text
    subname =cells[0].find('small')
    if subname:
      actual +=f'({subname.text})'
    evolucion=cells[2].find('a',class_='ent-name').text
    subname2 =cells[2].find('small')
    if subname2:
      evolucion +=f'({subname2.text})'
    nivel=cells[3].text
    desc=cells[4].text

    # Print item data
    #print("Pokedex number:",pokedex_number)
    #print("Name:",name)
    # Write item data on csv file
    enlistados.append({actual,evolucion})
    csv_writter.writerow([
      actual,evolucion,nivel,"null",f'Evolves at level {nivel} {desc}',"level"
    ])

url='https://pokemondb.net/evolution/stone'

# HTTP request
response =requests.get(url)

# BeautifulSoup object
soup= BeautifulSoup(response.text,'html.parser')


# find all pokemons
items_table=soup.find('table',class_='data-table')
items=items_table.find_all('tr')
# Travel around rows
for item in items:
  #obtain all columns of each row
  cells=item.find_all('td')
  if cells:
    actual=cells[0].find('a',class_='ent-name').text
    subname =cells[0].find('small')
    if subname:
      actual +=f'({subname.text})'
    evolucion=cells[2].find('a',class_='ent-name').text
    subname2 =cells[2].find('small')
    if subname2:
      evolucion +=f'({subname2.text})'
    item=cells[3].find('a').text
    desc=cells[3].text

    # Print item data
    #print("Pokedex number:",pokedex_number)
    #print("Name:",name)
    # Write item data on csv file
    enlistados.append({actual,evolucion})
    csv_writter.writerow([
      actual,evolucion,0,item,f'Evolves with {desc}',"stone"
    ])
    
url='https://pokemondb.net/evolution/trade'

# HTTP request
response =requests.get(url)

# BeautifulSoup object
soup= BeautifulSoup(response.text,'html.parser')


# find all pokemons
items_table=soup.find('table',class_='data-table')
items=items_table.find_all('tr')
# Travel around rows
for item in items:
  #obtain all columns of each row
  cells=item.find_all('td')
  if cells:
    actual=cells[0].find('a',class_='ent-name').text
    subname =cells[0].find('small')
    if subname:
      actual +=f'({subname.text})'
    evolucion=cells[2].find('a',class_='ent-name').text
    subname2 =cells[2].find('small')
    if subname2:
      evolucion +=f'({subname2.text})'
    try:
      item=cells[3].find('a').text
    except:
      item="null"
    desc=cells[3].text

    # Print item data
    #print("Pokedex number:",pokedex_number)
    #print("Name:",name)
    # Write item data on csv file
    enlistados.append({actual,evolucion})
    csv_writter.writerow([
      actual,evolucion,0,item,f'Evolves being traded, {desc}',"trade"
    ])
    

url='https://pokemondb.net/evolution/friendship'

# HTTP request
response =requests.get(url)

# BeautifulSoup object
soup= BeautifulSoup(response.text,'html.parser')


# find all pokemons
items_table=soup.find('table',class_='data-table')
items=items_table.find_all('tr')
# Travel around rows
for item in items:
  #obtain all columns of each row
  cells=item.find_all('td')
  if cells:
    actual=cells[0].find('a',class_='ent-name').text
    subname =cells[0].find('small')
    if subname:
      actual +=f'({subname.text})'
    evolucion=cells[2].find('a',class_='ent-name').text
    subname2 =cells[2].find('small')
    if subname2:
      evolucion +=f'({subname2.text})'
    desc=cells[3].text

    # Print item data
    #print("Pokedex number:",pokedex_number)
    #print("Name:",name)
    # Write item data on csv file
    enlistados.append({actual,evolucion})
    csv_writter.writerow([
      actual,evolucion,0,"null",f'evolves through friendship {desc}',"friendship"
    ])
    


url='https://pokemondb.net/evolution/status'

# HTTP request
response =requests.get(url)

# BeautifulSoup object
soup= BeautifulSoup(response.text,'html.parser')


# find all pokemons
items_table=soup.find('table',class_='data-table')
items=items_table.find_all('tr')
# Travel around rows
for item in items:
  #obtain all columns of each row
  cells=item.find_all('td')
  if cells:
    actual=cells[0].find('a',class_='ent-name').text
    subname =cells[0].find('small')
    if subname:
      actual +=f'({subname.text})'
    evolucion=cells[2].find('a',class_='ent-name').text
    subname2 =cells[2].find('small')
    if subname2:
      evolucion +=f'({subname2.text})'
    desc=cells[4].text
    try:
      item=cells[4].find('a').text
    except:
      item="null"

    if{actual,evolucion} not in enlistados:
      csv_writter.writerow([
        actual,evolucion,0,item,desc,"status"
      ])
    