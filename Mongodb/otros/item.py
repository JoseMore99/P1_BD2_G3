import ast
import pandas as pd
import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["pokemondb"]
collection = db["items"]
def convertir_a_cadena(numero):
    return str(numero).zfill(4)
data = pd.read_csv('J:/universidad/bases 2/P1_BD2_G3/otros/items.csv')

# Acceder a las columnas por nombre
name = data['name']
efect = data['effect']
cat = data['cathegory']
for i in range(len(name)):
    valores={
        "name":name.iloc[i]  
    }
    if  str(efect.iloc[i])!="nan":
        valores["efect"]=str(efect.iloc[i])    
    elif str(cat.iloc[i])!="nan":
        valores["cathegory"]=str(cat.iloc[i])
    collection.insert_one(valores)