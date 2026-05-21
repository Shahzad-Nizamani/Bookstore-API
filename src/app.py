from src.routes.update_book import router as update_book_router
from src.routes.add_book import router as add_book_router
from src.routes.get_books import router as get_books_router
from src.routes.get_signle_book import router as get_single_book_router
from src.routes.delete_book import router as delete_book_router
from fastapi import FastAPI

app = FastAPI()
app.include_router(update_book_router)
app.include_router(add_book_router) 
app.include_router(get_books_router)
app.include_router(get_single_book_router)
app.include_router(delete_book_router)