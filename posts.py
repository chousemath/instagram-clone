# for Thaty
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

app = FastAPI()

class Post(BaseModel):
    image_urls: list[str]
    like_count: int
    comment_count: int
    creator: str
    description: str

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get('/posts')
def get_posts():
    '''
    Should fetch all posts from the database
    '''
    posts = db.posts.find({})
    post_list = []
    for post in posts:
        post['_id'] = str(post['_id'])
        post_list.append(post)
        pass
    return {'posts': post_list}

@app.get('/posts/{_id}')
def get_post(_id: str):
    post = db.posts.find_one({'_id': ObjectId(_id)})
    post['_id'] = str(post['_id'])
    return post

@app.post("/posts")
async def create_post(post: Post):
    db.posts.insert_one(post.dict())
    return {'ok': True}

@app.put('/posts/{_id}')
async def update_post(_id: str, post: Post):
    db.posts.update_one(
        {'_id': ObjectId(_id)},
        {'$set': post.dict()}
    )
    return {'ok': True}

@app.delete('/posts/{_id}')
def delete_post(_id: str):
    db.posts.delete_one({'_id': ObjectId(_id)})
    return {'ok': True}