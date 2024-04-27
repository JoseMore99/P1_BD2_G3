import ast
import pandas as pd
import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["pokemondb"]
collection = db["pokemons"]
def convertir_a_cadena(numero):
    return str(numero).zfill(4)
# Leer el archivo CSV usando pandas
data = pd.read_csv('J:/universidad/bases 2/P1_BD2_G3/pokemons/Breeding.csv')

# pokedex_id,Egg_groups,gender_male ,gender_female ,egg_cycles
pokedex_id = data['pokedex_id']
gender_male = data['gender_male']
gender_female = data['gender_female']
egg_cycles = data['egg_cycles']
Egg_groups = data['Egg_groups']
Egg_groups= Egg_groups.apply(ast.literal_eval)
for i in range(len(pokedex_id)):
    documento = { 
        "egg_groups":Egg_groups.iloc[i],
        "gender_male":str(gender_male.iloc[i])+"%",
        "gender_female":str( gender_female.iloc[i])+"%",
        "egg_cycles":egg_cycles.iloc[i]
                     }
    filtro={"pokedex_id":convertir_a_cadena(pokedex_id.iloc[i])}
    collection.update_many(filtro, {"$set": {"breeding": documento}})
    