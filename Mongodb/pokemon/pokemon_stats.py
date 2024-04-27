import pandas as pd
import pymongo
import csv

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["pokemondb"]
collection = db["pokemons"]
data = pd.read_csv('J:/universidad/bases 2/P1_BD2_G3/pokemons/pokemons_2.csv')

# pokedex_number,name,types,total,hp,attack,defense,special_attack,special_defense,speed,total
name = data['name']
hp = data['hp']
attack = data['attack']
defense = data['defense']
special_attack = data['special_attack']
special_defense = data['special_defense']
speed = data['speed']
total = data['total']
for i in range(len(name)):
        print()
        documento = { "hp":int(hp.iloc[i]),
                     "attack":int( attack.iloc[i]),
                     "defense":int(defense.iloc[i]),
                     "special_attack":int(special_attack.iloc[i]),
                     "special_defense":int(special_defense.iloc[i]),
                     "speed":int(speed.iloc[i]),
                     "total":int(total.iloc[i])
                     }
        filtro={"name":name.iloc[i]}
        collection.update_many(filtro, {"$set": {"stats": documento}})