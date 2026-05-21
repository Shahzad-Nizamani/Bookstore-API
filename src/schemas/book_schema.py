from pydantic import BaseModel
from datetime import date
from typing import Optional

class BookCreate(BaseModel):
    title: str
    author: str
    price: float
    isbn: str
    published_date: date

class BookUpdate(BaseModel):
    title: Optional[str] = None
    author: Optional[str] = None
    price: Optional[float] = None
    isbn: Optional[str] = None
    published_date: Optional[date] = None

class BookResponse(BaseModel):
    id: int
    title: str
    author: str
    price: float
    isbn: str
    published_date: Optional[date] = None

    class Config:
        from_attributes = True
