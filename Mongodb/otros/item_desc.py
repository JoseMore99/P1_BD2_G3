import ast
import pandas as pd
import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["pokemondb"]
collection = db["items"]
def convertir_a_cadena(numero):
    return str(numero).zfill(4)
# Leer el archivo CSV usando pandas
data = pd.read_csv('J:/universidad/bases 2/P1_BD2_G3/otros/items_desc.csv')

# Acceder a las columnas por nombre
name = data['name']
games = data['game']
descriptions = data['description']
games= games.apply(ast.literal_eval)
for i in range(len(name)):
    for j in games.iloc[i]:
        documento={}
    filtro={"name":name.iloc[i]}
    documento = collection.find_one(filtro)
    for j in games.iloc[i]:
        try:
            documento["desc_gen_game"][j]=str(descriptions.iloc[i])
        except:
            documento["desc_gen_game"]={j:str(descriptions.iloc[i])}

    collection.update_many(filtro, {"$set": {"desc_gen_game": documento["desc_gen_game"]}})