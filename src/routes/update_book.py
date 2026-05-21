from fastapi.routing import APIRouter
from src.controllers.update_book import update_book
from src.models.update_book_model import UpdateBook

router = APIRouter()

@router.put("/books/{id}")
def update_book_endpoint(id: int, body: UpdateBook):
    # remove None values — only keep what user provided
    update_data = body.model_dump(exclude_none=True)
    return update_book(id, **update_data)
