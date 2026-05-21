from src.db.db_conn import SessionLocal
from src.models.book import book

def fetch_all_books():

    session = SessionLocal()
    books = session.query(book).all()
    session.close()
    return books