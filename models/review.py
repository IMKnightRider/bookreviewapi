from pydantic import BaseModel

class Review(BaseModel):
    id: str
    book_id: str
    user_id: str
    rating: float
    comment: str