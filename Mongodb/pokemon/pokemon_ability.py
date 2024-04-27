import ast
import pandas as pd
import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["pokemondb"]
collection = db["pokemons"]
def convertir_a_cadena(numero):
    return str(numero).zfill(4)
# Leer el archivo CSV usando pandas
data = pd.read_csv('J:/universidad/bases 2/P1_BD2_G3/pokemons/pokemon_ability.csv')

#pokedex_id,abilities
pokedex_id = data['pokedex_id']
abilities = data['abilities']
abilities= abilities.apply(ast.literal_eval)
for i in range(len(pokedex_id)):
    filtro={"pokedex_id":convertir_a_cadena(pokedex_id.iloc[i])}
    collection.update_many(filtro, {"$set": {"abilities": abilities.iloc[i]}})

