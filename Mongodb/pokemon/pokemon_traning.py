import ast
import pandas as pd
import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["pokemondb"]
collection = db["pokemons"]
def convertir_a_cadena(numero):
    return str(numero).zfill(4)
data = pd.read_csv('J:/universidad/bases 2/P1_BD2_G3/pokemons/Training.csv')

#pokedex_id,EV_yield,catch_rate,base_friendship,base_exp,growth_rate cles
pokedex_id = data['pokedex_id']
EV_yield = data['EV_yield']
catch_rate = data['catch_rate']
base_friendship = data['base_friendship']
base_exp = data['base_exp']
growth_rate = data['growth_rate']
for i in range(len(pokedex_id)):
    if base_exp.iloc[i]!='—':

        documento = { 
            "EV_yield":EV_yield.iloc[i],
            "catch_rate":str(catch_rate.iloc[i]),
            "base_friendship":str( base_friendship.iloc[i]),
            "base_exp":int( base_exp.iloc[i]),
            "growth_rate":growth_rate.iloc[i]
                        }
    else:
        documento = { 
            "EV_yield":EV_yield.iloc[i],
            "catch_rate":str(catch_rate.iloc[i]),
            "growth_rate":growth_rate.iloc[i]
                        }
    filtro={"pokedex_id":convertir_a_cadena(pokedex_id.iloc[i])}
    collection.update_many(filtro, {"$set": {"training": documento}})

