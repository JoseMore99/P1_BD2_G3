import ast
import pandas as pd
import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["pokemondb"]
collection = db["pokemons"]
def convertir_a_cadena(numero):
    return str(numero).zfill(4)
# Leer el archivo CSV usando pandas

# Leer el archivo CSV usando pandas
data = pd.read_csv('J:/universidad/bases 2/P1_BD2_G3/pokemons/pokemon_move_bylevel.csv')

# pokedex_id,move_name,level
pokedex_id = data['pokedex_id']
move_name = data['move_name']
level = data['level']
for i in range(len(pokedex_id)):
    documento={}
    filtro={"pokedex_id":convertir_a_cadena(pokedex_id.iloc[i])}

    collection.update_many(filtro, {"$addToSet": {"moves_bylevel": {"move_name":move_name.iloc[i],"level":int(level.iloc[i])}}})