from pydantic import BaseModel, Field,EmailStr
from datetime import datetime, timedelta

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str = None or None

class User(BaseModel):
    username: str
    email: str = None or None
    full_name: str = None
    disabled: bool = None
    
class UserInDB(User):
    hashed_password: str