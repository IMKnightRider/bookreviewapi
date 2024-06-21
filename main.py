from fastapi import FastAPI

# Mongo Db Connection Code
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
uri = "mongodb+srv://sectionc90:SYn0GnMkENvqRD7M@review.cnwhjqg.mongodb.net/?retryWrites=true&w=majority&appName=review"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

app = FastAPI()

