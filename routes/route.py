from fastapi import APIRouter
from models.book import Book
from config.database import collection_name
from models.user import User
from schema.schemas import list_serial, user_serial
from bson import ObjectId

router = APIRouter()

# get Request Methods
@router.get("/books")
async def get_books():
    books = collection_name.find()
    return list_serial(books)

@router.get("/user/{user_id}")
async def get_user(user_id: str):
    user = user.find_one({"_id": ObjectId(user_id)})
    return user_serial(user)


# Post Request Methods
@router.post("/books")
async def add_book(book: Book):
    book = dict(book)
    collection_name.insert_one(book)
    return {"message": "Book added successfully"}

# @router.post("/user")
# async def add_user(user: User):
#     user = dict(user)
#     user.insert_one(user)
#     return {"message": "User added successfully"}

# Put Request Methods
@router.put("/books/{book_id}")
async def update_book(book_id: str, book: Book):
    collection_name.update_one({"_id": ObjectId(book_id)}, {"$set": dict(book)})
    return {"message": "Book updated successfully"}


# Delete Request Methods
@router.delete("/books/{book_id}")
async def delete_book(book_id: str):
    collection_name.delete_one({"_id": ObjectId(book_id)})
    return {"message": "Book deleted successfully"}
