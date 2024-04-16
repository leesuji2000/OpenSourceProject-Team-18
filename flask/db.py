from flask import Flask
from flask_pymongo import pymongo
from index import index
CONNECTION_STRING = "mongodb+srv://id:passwordP@boca.dm5skx7.mongodb.net/?retryWrites=true&w=majority&appName=boca"
client = pymongo.MongoClient(CONNECTION_STRING)
db = client.get_database('baca')
user_collection = pymongo.collection.Collection(db, 'boca')