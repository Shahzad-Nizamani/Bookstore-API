from pydantic import BaseModel
from typing import Optional

class UpdateBook(BaseModel):
    title: Optional[str] = None
    author: Optional[str] = None
    price: Optional[float] = None
    isbn: Optional[str] = None
    published_date: Optional[str] = None