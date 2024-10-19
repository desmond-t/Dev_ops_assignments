# To install flask, first run the following line in the terminal:
# pip install flask

# To import the flask into the project use the following line:
from flask import Flask
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

username = os.getenv('MONGODB_USERNAME')
password = os.getenv('MONGODB_PASSWORD')

connection_string = f"mongodb+srv://{username}:{password}@cluster0.bb9ww.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
print(f"Username: {username}, Password: {password}")
flask_app = Flask(__name__)



# MongoDB Atlas Connection
client = MongoClient(connection_string)
db = client.app  # Replace "app" with your database name
products_collection = db.products  # Replace products with your collection name

from app import routes