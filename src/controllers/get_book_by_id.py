from src.db.db_conn import SessionLocal
from src.models.book import book

def fetch_book_by_id(book_id):

    session = SessionLocal()
    book_data = session.query(book).filter(book.id == book_id).first()
    session.close()
    return book_data