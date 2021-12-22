from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
from pymongo import MongoClient
from dotenv import load_dotenv
from os import environ
from bson.objectid import ObjectId
load_dotenv()

key = environ['MONGODB_CONNECTION_STRING']

client = MongoClient(key)
db = client.wcoding

class Product(BaseModel):
    name: str
    price: int

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get('/products')
def get_products():
    '''
    Should fetch all products from the database
    '''
    products = db.products.find({})
    product_list = []
    for product in products:
        product['_id'] = str(product['_id'])
        product_list.append(product)
    return {'products': product_list}

@app.get('/products/{_id}')
def get_product(_id: str):
    product = db.products.find_one({'_id': ObjectId(_id)}) # None
    product['_id'] = str(product['_id'])
    return product

@app.post("/products")
async def create_product(product: Product):
    db.products.insert_one(product.dict())
    return {'ok': True}

@app.put('/products/{_id}')
async def update_product(_id: str, product: Product):
    db.products.update_one(
        {'_id': ObjectId(_id)},
        {'$set': product.dict()}
    )
    return {'ok': True}

@app.delete('/products/{_id}')
def delete_product(_id: str):
    db.products.delete_one({'_id': ObjectId(_id)})
    return {'ok': True}