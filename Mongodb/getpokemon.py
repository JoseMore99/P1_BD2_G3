import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["pokemondb"]
collection = db["pokemons"]


resultado = collection.find_one({"pokedex_id": "1009"})
print(resultado)

resultado = collection.find_one({"pokedex_id": "0500"})
print(resultado)