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

class User(BaseModel):
    name: str
    birthdate: Optional[str]
    profile_image_url: Optional[str]
    username: str
    website: Optional[str]
    pronouns: Optional[list[str]]
    biography: Optional[str]
    email: Optional[str]
    phone: Optional[int]
    gender: Optional[str]

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "Hi"}

@app.post("/users")
async def create_new_user(user: User):
    db.users.insert_one(user.dict())
    return {'message': 'A new user was saved to the database'}

@app.put('/users/{_id}')
async def update_user(_id: str, user: User):
    db.users.update_one(
        {'_id': ObjectId(_id)},
        {'$set': user.dict()}
    )
    return {'updated': True}

@app.get('/users')
def get_all_users():
    users = db.users.find({})
    user_list = []
    for user in users:
        user['_id'] = str(user['_id'])
        user_list.append(user)
    return {'users': user_list}

@app.get('/users/{_id}')
def find_single_user(_id: str):
    user = db.users.find_one({'_id': ObjectId(_id)})
    user['_id'] = str(user['_id'])
    return user

@app.delete('/users/{_id}')
def delete_users(_id: str):
    db.users.delete_one({'_id': ObjectId(_id)})
    return {'deleted': True}

