# To install flask, first run the following line in the terminal:
# pip install flask

# To import the flask into the project use the following line:
from flask import Flask
from pymongo import MongoClient

flask_app = Flask(__name__)

# MongoDB Atlas Connection
client = MongoClient("mongodb+srv://root:dfCkwqLIy8Hh42Xh@cluster0.aye3c.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client.shop_db  # Replace "app" with your database name
products_collection = db.products  # Replace products with your collection name

from app import routes