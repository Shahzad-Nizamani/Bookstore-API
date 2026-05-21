from src.db.db_conn import SessionLocal
from src.models.book import book

def delete_book(book_id):

    session = SessionLocal()
    book_data = session.query(book).filter(book.id == book_id).first()
    if book_data:
        session.delete(book_data)
        session.commit()
        return {"response": "Book deleted successfully"}
    else:
        return None