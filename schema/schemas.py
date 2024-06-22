def individual_serial(book) -> dict:
    return {
        "book_id": str(book["_id"]),
        "title": book["title"],
        "author": book["author"],
        "genre": book["genre"],
        "year": book["year"],
        "rating": book["rating"],
        "reviews": book["reviews"]
    }

def user_serial(user) -> dict:
    return {
        "user_id": str(user["_id"]),
        "name": user["name"],
        "email": user["email"],
        "password": user["password"],
        "author": user["author"]
    }

def list_serial(books) -> list:
    return [individual_serial(book) for book in books]