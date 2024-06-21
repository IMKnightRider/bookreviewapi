from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://admin:test1234@review.cnwhjqg.mongodb.net/?retryWrites=true&w=majority&appName=review"

client = MongoClient(uri)

db = client.book_review
collection_name = db["review_collection"]
new1 = db["new_collection"]
