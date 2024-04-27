import ast
import pandas as pd
import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["pokemondb"]
collection = db["moves"]
def convertir_a_cadena(numero):
    return str(numero).zfill(4)
# Leer el archivo CSV usando pandas
data = pd.read_csv('J:/universidad/bases 2/P1_BD2_G3/movimientos/moviminetos9.csv')

# name,types,power,Category,acc,pp,efect
name = data['name']
types = data['types']
power = data['power']
Category = data['Category']
acc = data['acc']
pp = data['pp']
efect = data['efect']
for i in range(len(name)):
    valores={
        "name":name.iloc[i]  
    }
    valores["Acc"]="∞"
    if  str(efect.iloc[i])!="nan":
           valores["Efect"]=str(efect.iloc[i])
    if  str(power.iloc[i])!="—":
           valores["Power"]=int(power.iloc[i])
    if  str(acc.iloc[i])!="—":
           valores["Acc"]=int(acc.iloc[i])
    if  str(pp.iloc[i])!="—":
           valores["Pp"]=int(pp.iloc[i])
    if  str(Category.iloc[i])!="nan":
           valores["Category"]=str(Category.iloc[i])
    if  str(types.iloc[i])!="nan":
           valores["type"]=str(types.iloc[i])
    
    collection.insert_one(valores)