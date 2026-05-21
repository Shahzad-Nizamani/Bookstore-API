from fastapi import APIRouter
from src.controllers.get_books import fetch_all_books

router = APIRouter()

@router.get("/books")
def get_books_endpoint():
    return fetch_all_books()