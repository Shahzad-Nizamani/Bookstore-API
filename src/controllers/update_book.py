from src.db.db_conn import SessionLocal
from src.models.book import book
from fastapi import HTTPException

def update_book(id, **kwargs):

    Session = SessionLocal()
    # fetch the book
    book_record = Session.query(book).filter(book.id == id).first()
    
    if not book_record:
        raise HTTPException(status_code=404, detail="Book not found")
        
    # allowed fields to update
    allowed_fields = {"title", "author", "price", "isbn", "published_date"}
    
    # update only the fields the user provided
    for key, value in kwargs.items():
        if key in allowed_fields:
            setattr(book_record, key, value)
    
    Session.commit()
    Session.refresh(book_record)
    return {"response": "Book updated successfully"}