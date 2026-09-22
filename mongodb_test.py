from pymongo import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://nks101100_db_user:Nikhil%40989344@cluster0.atpgemz.mongodb.net/?appName=Cluster0"

client = MongoClient(uri, server_api=ServerApi('1'))

try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)