from pymongo.mongo_client import MongoClient

passwd = "Kh0BblepkIbcE5tm"
uri = f"mongodb+srv://kumarp73616:{passwd}@bookreview.0xpa7cl.mongodb.net/?retryWrites=true&w=majority&appName=Bookreview"
client = MongoClient(uri)

db = client.book_review
collection_name = db["book_collection"]
user_collection = db["user_collection"]
