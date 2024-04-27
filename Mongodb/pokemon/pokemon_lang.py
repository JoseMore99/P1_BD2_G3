import ast
import pandas as pd
import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["pokemondb"]
collection = db["pokemons"]
def convertir_a_cadena(numero):
    return str(numero).zfill(4)
# Leer el archivo CSV usando pandas
data = pd.read_csv('J:/universidad/bases 2/P1_BD2_G3/pokemons/pokemon_languages.csv')

# Evolving_from,Evolving_to,level,item,description,type
pokedex_id = data['pokedex_id']
language = data['language']
name = data['name']
for i in range(len(pokedex_id)):
        documento={}
        filtro={"pokedex_id":convertir_a_cadena(pokedex_id.iloc[i])}
        documento = collection.find_one(filtro)
        try:
                documento["languages"][language.iloc[i]]=str(name.iloc[i])
        except:
                documento["languages"]={language.iloc[i]:str(name.iloc[i])}
        #print( documento["desc_gen_game"])
        # a = input("jiji")
        collection.update_many(filtro, {"$set": {"languages": documento["languages"]}})