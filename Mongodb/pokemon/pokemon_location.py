import ast
import pandas as pd
import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["pokemondb"]
collection = db["pokemons"]
def convertir_a_cadena(numero):
    return str(numero).zfill(4)
data = pd.read_csv('J:/universidad/bases 2/P1_BD2_G3/pokemons/pokemon_location.csv')

# pokedex_id,game,location 
pokedex_id = data['pokedex_id']
game = data['game']
location = data['location']
game= game.apply(ast.literal_eval)
for i in range(len(pokedex_id)):
    documento={}
    filtro={"pokedex_id":convertir_a_cadena(pokedex_id.iloc[i])}
    documento = collection.find_one(filtro)
    for j in game.iloc[i]:
        lugar = str(location.iloc[i]).split(", ")
        for k in range(len(lugar)):
            if lugar[k].isdigit():
                lugar[k] = "Route "+lugar[k]
        documento["location"][j]=lugar
    collection.update_many(filtro, {"$set": {"location": documento["location"]}})
    #print(documento["location"])
    #a = input("jiji")
        #print(lugar)
