from fastapi import APIRouter, HTTPException
from src.controllers.get_book_by_id import fetch_book_by_id

router = APIRouter()
 
@router.get("/books/{id}")
def get_book_by_id_endpoint(id: int):
    
    book_data = fetch_book_by_id(id)
    if not book_data:
        raise HTTPException(status_code=404, detail="Book not found")
    return book_data