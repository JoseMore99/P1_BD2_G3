import pymongo

# Establecer la conexión con el servidor MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")

# Seleccionar la base de datos
db = client["Usac"]

# Acceder a una colección
collection = db["usac1"]

# Ejemplo de inserción de un documento
documento = {"id":3,"nombre": "Ejemplo", "edad": 30}
#collection.insert_one(documento)
#collection.delete_many(documento)
#collection.delete_many({}) para eliminar todo}
#collection.delete_one(documento)

# Ejemplo de búsqueda de un documento
resultado = collection.find_one({"nombre": "Ejemplo"})
print(resultado)
resultado = collection.find_one({"nombre": "Jose"})
print(resultado)
resultado = collection.find()
for i in resultado:
    print(i)