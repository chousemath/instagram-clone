from datetime import datetime
from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
from pymongo import MongoClient
from dotenv import load_dotenv
from os import environ
import certifi
from pprint import pprint
from bson.objectid import ObjectId
load_dotenv()

key = environ ['MONGODB_CONNECTION_STRING']

client = MongoClient(key, tlsCAFile=certifi.where())
db = client.wcoding

class Comment(BaseModel):
    user_id: str
    creator: str
    body: str
    created_at: datetime
    updated_at: datetime

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get('/comments')
def get_comments():
    '''
    Should fetch all comments from the database
    '''
    comments = db.comments.find({})
    comment_list = []
    for comment in comments:
        comment['_id'] = str(comment['_id'])
        comment_list.append(comment)
    return {'comments': comment_list}

@app.get('/comments/{_id}')
def get_comment(_id: str):
    comment = db.comments.find_one({'_id': ObjectId(_id)}) # None
    comment['_id'] = str(comment['_id'])
    return comment

@app.post("/comments")
async def create_comment(comment: Comment):
    db.comments.insert_one(comment.dict())
    return {'ok': True}

@app.put('/comments/{_id}')
async def update_comment(_id: str, comment: Comment):
    db.comments.update_one(
        {'_id': ObjectId(_id)},
        {'$set': comment.dict()}
    )
    return {'ok': True}

@app.delete('/comments/{_id}')
def delete_comment(_id: str):
    db.comments.delete_one({'_id': ObjectId(_id)})
    return {'ok': True}