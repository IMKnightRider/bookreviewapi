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

def list_serial(books) -> list:
    return [individual_serial(book) for book in books]