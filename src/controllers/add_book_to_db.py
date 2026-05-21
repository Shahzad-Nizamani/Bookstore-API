from src.db.db_conn import SessionLocal
from src.models.book import book

def add_book(book_data):

    session = SessionLocal()
    new_book = book(**book_data.dict())
    session.add(new_book)
    session.commit()
    session.refresh(new_book)
    session.close()
    return {"response": "Book added successfully"}