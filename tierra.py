from pymongo import MongoClient
from dotenv import load_dotenv
from os import environ
from pprint import pprint
from bson.objectid import ObjectId
load_dotenv()

key = environ['MONGODB_CONNECTION_STRING']

#print(key)

client = MongoClient(key)
db = client.wcoding

doc = {
    'name': 'Tierra Thompson',
    'message': 'Hello~'
}
#insert a single document into collection called test
#db.test.insert_one(doc)

#doc = db.test.find_one({'name': 'Tierra Thompson'})
#doc = db.text.find_one({'_id': ObjectId('61b9d713d17b5b25c51f8cdf')})

#pprint(doc)

#finding multiple documents from collection
#docs = db.test.find({'name': 'Tierra Thompson'})

#for doc in docs:
    #pprint(doc)

db.test.update_one(
    {
        '_id': ObjectId('61beb27e2d298a9f6b124b43')
    }, #how to know which document to update
    {
        '$set': {
            'name': 'Sarah Smith',
            'message': 'Goodbye',
            'age': 30,
            'hobbies': ['cooking', 'reading']
        }
    }) #how to update document


#doc = db.test.find_one({'_id': ObjectId('61beb27e2d298a9f6b124b43')})
#pprint(doc)

#example of deleting
res = db.test.delete_one({'_id': ObjectId('61b9d720947e6fdaf0b42916')})
print(res.acknowledged)

print(res.deleted_count)