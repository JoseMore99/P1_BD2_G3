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
    documento={}
    filtro={"name":abilities.iloc[i]}
    documento = collection.find_one(filtro)
    for j in games.iloc[i]:
        try:
            documento["desc_gen_game"][j]=str(descriptions.iloc[i])
        except:
            documento["desc_gen_game"]={j:str(descriptions.iloc[i])}

    collection.update_many(filtro, {"$set": {"desc_gen_game": documento["desc_gen_game"]}})