import pymongo
import csv

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["pokemondb"]
collection = db["pokemons"]
with open('J:/universidad/bases 2/P1_BD2_G3/pokemons/pokemon_indi.csv', newline='') as archivo_csv:
    lector_csv = csv.reader(archivo_csv)
    for indice, f in enumerate(lector_csv):
        if indice == 0:
            continue
        documento = {"pokedex_id":f[0],"name": f[1], "especie":f[2],"height": f[3],"weight":f[4]}
        collection.insert_one(documento)
                

# Establecer la conexión con el servidor MongoDB
