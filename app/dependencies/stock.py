from flask import Flask
from flask_pymongo import pymongo
from app import app

CONNECTION_STRING = "mongodb+srv://admin:admin@cluster0-hsmxr.gcp.mongodb.net/test?retryWrites=true&w=majority"

client = pymongo.MongoClient(CONNECTION_STRING)
db = client.get_database('stocks')
user_collection = pymongo.collection.Collection(db, 'performanceData')

class Stock:
	def __init__():
		
	def getStock():
	    stockValue = db.user_collection.find_one({"name": "John"})
	    return stockValue;

	getStock()