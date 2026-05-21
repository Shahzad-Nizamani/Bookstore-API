from fastapi import APIRouter
from src.schemas.book_schema import BookCreate
from src.controllers.add_book_to_db import add_book
router = APIRouter()

@router.post("/books")
def add_book_endpoint(book_data: BookCreate):
    return add_book(book_data)