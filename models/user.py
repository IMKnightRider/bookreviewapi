from pydantic import BaseModel

class User:
    name: str
    email: str
    password: str
    author: bool
