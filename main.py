from typing import Optional
from datetime import datetime
from fastapi import FastAPI
from pydantic import BaseModel
from pymongo import MongoClient
from dotenv import load_dotenv
from os import environ
import certifi
from pprint import pprint
from bson.objectid import ObjectId

load_dotenv()

key = environ["MONGODB_CONNECTION_STRING"]

client = MongoClient(key, tlsCAFile=certifi.where())
db = client.wcoding

app = FastAPI()


class Product(BaseModel):
    name: str
    price: int


class Post(BaseModel):
    image_urls: list[str]
    like_count: int
    comment_count: int
    creator: str
    description: str


class Comment(BaseModel):
    creator: str
    body: str
    created_at: datetime
    updated_at: datetime


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/products")
def get_products():
    """
    Should fetch all products from the database
    """
    products = db.products.find({})
    product_list = []
    for product in products:
        product["_id"] = str(product["_id"])
        product_list.append(product)
    return {"products": product_list}


@app.get("/products/{_id}")
def get_product(_id: str):
    product = db.products.find_one({"_id": ObjectId(_id)})  # None
    product["_id"] = str(product["_id"])
    return product


@app.post("/products")
async def create_product(product: Product):
    db.products.insert_one(product.dict())
    return {"ok": True}


@app.put("/products/{_id}")
async def update_product(_id: str, product: Product):
    db.products.update_one({"_id": ObjectId(_id)}, {"$set": product.dict()})
    return {"ok": True}


@app.delete("/products/{_id}")
def delete_product(_id: str):
    db.products.delete_one({"_id": ObjectId(_id)})
    return {"ok": True}


@app.get("/comments")
def get_comments():
    """
    Should fetch all comments from the database
    """
    comments = db.comments.find({})
    comment_list = []
    for comment in comments:
        comment["_id"] = str(comment["_id"])
        comment_list.append(comment)
    return {"comments": comment_list}


@app.get("/comments/{_id}")
def get_comment(_id: str):
    comment = db.comments.find_one({"_id": ObjectId(_id)})  # None
    comment["_id"] = str(comment["_id"])
    return comment


@app.post("/comments")
async def create_comment(comment: Comment):
    db.comments.insert_one(comment.dict())
    return {"ok": True}


@app.put("/comments/{_id}")
async def update_comment(_id: str, comment: Comment):
    db.comments.update_one({"_id": ObjectId(_id)}, {"$set": comment.dict()})
    return {"ok": True}


@app.delete("/comments/{_id}")
def delete_comment(_id: str):
    db.comments.delete_one({"_id": ObjectId(_id)})
    return {"ok": True}


@app.get("/posts")
def get_posts():
    """
    Should fetch all posts from the database
    """
    posts = db.posts.find({})
    post_list = []
    for post in posts:
        post["_id"] = str(post["_id"])
        post_list.append(post)
        pass
    return {"posts": post_list}


@app.get("/posts/{_id}")
def get_post(_id: str):
    post = db.posts.find_one({"_id": ObjectId(_id)})
    post["_id"] = str(post["_id"])
    return post


@app.post("/posts")
async def create_post(post: Post):
    db.posts.insert_one(post.dict())
    return {"ok": True}


@app.put("/posts/{_id}")
async def update_post(_id: str, post: Post):
    db.posts.update_one({"_id": ObjectId(_id)}, {"$set": post.dict()})
    return {"ok": True}


@app.delete("/posts/{_id}")
def delete_post(_id: str):
    db.posts.delete_one({"_id": ObjectId(_id)})
    return {"ok": True}
