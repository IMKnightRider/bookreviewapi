def individual_serial(book) -> dict:
    return {
        "book_id": str(book["_id"]),
        "title": book["title"],
        "author": book["author"],
        "genre": book["genre"],
        "year": book["year"],
        "rating": book["rating"],
        "reviews": book["reviews"],
        "img": book["img"],
    }

def user_serial(user) -> dict:
    return {
        "user_id": str(user["_id"]),
        "name": user["name"],
        "email": user["email"],
        "hashed_password": user["hashed_password"],
        "author": user["disabled"]
    }

def list_serial(books) -> list:
    return [individual_serial(book) for book in books]


def user_list(users) -> list:
    return [user_serial(user) for user in users]