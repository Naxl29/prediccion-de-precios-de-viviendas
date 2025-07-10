from pymongo import MongoClient

# Aquí se crea la conexión con el servidor de MongoDB
cliente = MongoClient("localhost:27017")

# Acá conectamos a la base de datos
db = cliente["dataset"]

# Conectamos a la colección
colleccion = db["viviendas"]

print("Conexión exitosa a la base de datos y colección.")