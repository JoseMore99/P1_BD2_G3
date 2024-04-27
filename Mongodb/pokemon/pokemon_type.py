import ast
import pandas as pd
import pymongo
import csv

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["pokemondb"]
collection = db["pokemons"]

data = pd.read_csv('J:/universidad/bases 2/P1_BD2_G3/pokemons/pokemons_2.csv')

# pokedex_number,name,types
pokedex_number = data['name']
types = data['types']
types= types.apply(ast.literal_eval)
anterior=""
for i in range(len(pokedex_number)):
    filtro={"name":pokedex_number.iloc[i]}
    collection.update_many(filtro, {"$set": {"type": types.iloc[i]}})