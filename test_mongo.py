from pymongo import MongoClient
import certifi

client = MongoClient(
    "mongodb+srv://akshay123:akshay123@ecomclustor1.vddmp.mongodb.net/",
    tls=True,
    tlsCAFile=certifi.where()
)

print(client.list_database_names())
