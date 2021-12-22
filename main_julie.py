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

class Comments(BaseModel):
    name: str
    price: int

app = FastAPI()