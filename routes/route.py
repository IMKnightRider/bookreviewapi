from fastapi import APIRouter
from models.book import Book
from config.database import collection_name
from schema.schemas import list_serial
from bson import ObjectId


router = APIRouter()

# get Request Methods
@router.get("/books")
async def get_books():
    books = collection_name.find()
    return list_serial(books)

# Post Request Methods
@router.post("/books")
async def add_book(book: Book):
    book = dict(book)
    collection_name.insert_one(book)
    return {"message": "Book added successfully"}