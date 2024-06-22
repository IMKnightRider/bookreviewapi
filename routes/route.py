from datetime import timedelta
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from scipy import stats
from config.auth import ACCESS_TOKEN_EXPIRE_MINUTES,create_user, authenticate_user, create_Access_token, get_current_user
from models.book import Book
from config.database import collection_name, user_collection
from models.user import Token, User
from schema.schemas import list_serial, user_list, user_serial
from bson import ObjectId

router = APIRouter()

# get Request Methods
@router.get("/books")
async def get_books():
    books = collection_name.find()
    return list_serial(books)

@router.get("/users")
async def get_users():
    users = user_collection.find()
    return user_list(users)

@router.get("/users/{user_id}")
async def get_user(id: str):
    user = user_collection.find_one({"_id": ObjectId(id)})
    return user_serial(user)



@router.get("/users/me", response_model=User)
async def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user

@router.get("/users/me/items")
async def read_own_items(current_user: User = Depends(get_current_user)):   
    return {"items": [{"item_id": "Foo", "owner": current_user.username}]}

@router.get("/user/login")
async def login_user(email: str, passwd: str):
    user = authenticate_user(user_collection, email, passwd)
    if not user:
        raise HTTPException(status_code=400, detail="Invalid credentials")
    
    return user_serial(user)

# Post Request Methods
@router.post("/books")
async def add_book(book: Book):
    book = dict(book)
    collection_name.insert_one(book)
    return {"message": "Book added successfully"}

@router.post("/user", response_model=User)
async def createUser(user: User, password: str):
    if user_collection.find_one({"email": user.email}):
        raise HTTPException(status_code=400, detail="Email already registered")
    
    user = create_user(user_collection, user, password)
    return {"message": "User created successfully"}


@router.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(user_collection, form_data.username, form_data.password)

    if not user:
         raise HTTPException(
              status_code=status.HTTP_401_UNAUTHORIZED,
              detail="Invalid username or password",
              headers={"WWW-Authenticate": "Bearer"},
         )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_Access_token(data={"sub": user["email"]}, expires_delta=access_token_expires)
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




