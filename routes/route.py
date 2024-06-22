from datetime import timedelta
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from scipy import stats
from config.auth import ACCESS_TOKEN_EXPIRE_MINUTES, authenticate_user, create_Access_token, get_current_user
from models.book import Book
from config.database import collection_name, user_collection
from models.user import Token, User
from schema.schemas import list_serial, user_serial
from bson import ObjectId

router = APIRouter()

# get Request Methods
@router.get("/books")
async def get_books():
    books = collection_name.find()
    return list_serial(books)

@router.get("/users/me", response_model=User)
async def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user

@router.get("/users/me/items")
async def read_own_items(current_user: User = Depends(get_current_user)):   
    return {"items": [{"item_id": "Foo", "owner": current_user.username}]}

# Post Request Methods
@router.post("/books")
async def add_book(book: Book):
    book = dict(book)
    collection_name.insert_one(book)
    return {"message": "Book added successfully"}

@router.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(user, form_data.username, form_data.password)
    user_collection.insert_one(user)
    if not user:
         raise HTTPException(
              status_code=stats.HTTP_401_UNAUTHORIZED,
              detail="Invalid username or password",
              headers={"WWW-Authenticate": "Bearer"},
         )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_Access_token(data={"sub": user.username}, expires_delta=access_token_expires)
    return {"access_token": access_token, "token_type": "bearer"}


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




