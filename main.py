from typing import Optional
from datetime import datetime
from fastapi import FastAPI
from starlette.responses import FileResponse 
from pydantic import BaseModel
from pymongo import MongoClient
from dotenv import load_dotenv
from os import environ, path
import certifi
from pprint import pprint
from bson.objectid import ObjectId

load_dotenv()

key = environ["MONGODB_CONNECTION_STRING"]

client = MongoClient(key, tlsCAFile=certifi.where())
db = client.wcoding

app = FastAPI()


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


class Product(BaseModel):
    name: str
    price: int


class Post(BaseModel):
    # comments for Thaty
    # please include a "user_id" field
    image_urls: list[str]
    like_count: int
    comment_count: int
    creator: str
    description: str


class Comment(BaseModel):
    # comments for Julie
    # please include a "user_id" field
    creator: str
    body: str
    created_at: datetime
    updated_at: datetime


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/admin/products")
def get_products():
    """
    Should display the admin page for Products
    """
    return FileResponse(path.join('static', 'products.html'))

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



@app.get("/admin/users")
def get_users():
    """
    Should display the admin page for users
    """
    return FileResponse(path.join('static', 'users.html'))

@app.post("/users")
async def create_new_user(user: User):
    db.users.insert_one(user.dict())
    return {"message": "A new user was saved to the database"}


@app.put("/users/{_id}")
async def update_user(_id: str, user: User):
    db.users.update_one({"_id": ObjectId(_id)}, {"$set": user.dict()})
    return {"updated": True}


@app.get("/users")
def get_all_users():
    users = db.users.find({})
    user_list = []
    for user in users:
        user["_id"] = str(user["_id"])
        user_list.append(user)
    return {"users": user_list}


@app.get("/users/{_id}")
def find_single_user(_id: str):
    user = db.users.find_one({"_id": ObjectId(_id)})
    user["_id"] = str(user["_id"])
    return user


@app.delete("/users/{_id}")
def delete_users(_id: str):
    db.users.delete_one({"_id": ObjectId(_id)})
    return {"deleted": True}


@app.get("/profile")
def get_profile():
    return FileResponse(path.join('static', 'profile.html'))

@app.post("/profile")
async def create_new_profile(user: User):
    db.users.insert_one(user.dict())
    return {"message": "A new user was saved to the database"}