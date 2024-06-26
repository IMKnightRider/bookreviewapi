from pydantic import BaseModel
# from datetime import date

class Book(BaseModel):
    title: str
    author: str
    genre: str
    year: int
    rating: float
    reviews: int