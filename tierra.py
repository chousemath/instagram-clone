from pymongo import MongoClient
from dotenv import load_dotenv
from os import environ
load_dotenv()

key = environ['MONGODB_CONNECTION_STRING']

#print(key)

client = MongoClient(key)
db = client.wcoding

doc = {
    'name': 'Tierra Thompson',
    'message': 'Hello~'
}

db.test.insert_one(doc)

