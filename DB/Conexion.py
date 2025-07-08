from pymongo import MongoClient

#aqui se crea la conexion con el servidor de MongoDB
cliente = MongoClient("localhost:27017")

#aca conectamos a la base de datos
db = cliente["dataset"]

#conectamos a la coleccion
colleccion = db["viviendas"]

print("Conexión exitosa a la base de datos y colección.")