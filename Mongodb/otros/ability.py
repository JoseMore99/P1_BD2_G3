import ast
import pandas as pd
import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["pokemondb"]
collection = db["abilities"]
def convertir_a_cadena(numero):
    return str(numero).zfill(4)
# Leer el archivo CSV usando pandas
data = pd.read_csv('J:/universidad/bases 2/P1_BD2_G3/otros/ability_all.csv')

# Acceder a las columnas por nombre
abilities = data['ability']
games = data['game']
descriptions = data['Description']
games= games.apply(ast.literal_eval)
anterior=""
for i in range(len(abilities)):
    #print(f"Ability: {abilities.iloc[i]}")
    #print(f"game: {games.iloc[i]}")
    valores={
       "name":abilities.iloc[i]  
    }
    if anterior==abilities.iloc[i]:
        continue
    else:
        collection.insert_one(valores)
        anterior=abilities.iloc[i]
    #for j in games.iloc[i]:
       # print(j)
    #print(f"Description: {descriptions.iloc[i]}")
    #print('-' * 20)  