from fastapi import APIRouter, HTTPException
from src.controllers.delete_book import delete_book

router = APIRouter()

@router.delete("/books/{id}")
def delete_book_endpoint(id: int):
    resp =  delete_book(id)

    if not resp:
        raise HTTPException(status_code=404, detail="Book not found")
    else:
        return resp