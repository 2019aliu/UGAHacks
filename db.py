from flask import Flask
from flask_pymongo import pymongo
from app import app

CONNECTION_STRING = "mongodb+srv://admin:admin@cluster0-hsmxr.gcp.mongodb.net/test?retryWrites=true&w=majority"
# for Python3.4 or later: mongodb://admin:<password>@cluster0-shard-00-00-hsmxr.gcp.mongodb.net:27017,cluster0-shard-00-01-hsmxr.gcp.mongodb.net:27017,cluster0-shard-00-02-hsmxr.gcp.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority
# 

client = pymongo.MongoClient(CONNECTION_STRING)
db = client.get_database('stocks')
user_collection = pymongo.collection.Collection(db, 'performanceData')