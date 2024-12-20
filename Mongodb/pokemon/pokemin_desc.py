import ast
import pandas as pd
import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["pokemondb"]
collection = db["pokemons"]
def convertir_a_cadena(numero):
    return str(numero).zfill(4)

# Leer el archivo CSV usando pandas
data = pd.read_csv('J:/universidad/bases 2/P1_BD2_G3/pokemons/pokemon_desc.csv')

pokedex_id = data['pokedex_id']
games = data['game']
descriptions = data['description']
games= games.apply(ast.literal_eval)
for i in range(len(pokedex_id)):
    documento={}
    filtro={"pokedex_id":convertir_a_cadena(pokedex_id.iloc[i])}
    documento = collection.find_one(filtro)
    for j in games.iloc[i]:
        documento["desc_gen_game"][j]=str(descriptions.iloc[i])
    #print( documento["desc_gen_game"])
   # a = input("jiji")
    collection.update_many(filtro, {"$set": {"desc_gen_game": documento["desc_gen_game"]}})