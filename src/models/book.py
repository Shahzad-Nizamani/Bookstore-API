from sqlalchemy import Column, Integer, String, Date, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class book(Base):

    __tablename__ = "books"

    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    author = Column(String(50), nullable=False)
    price = Column(Float(10, 2), nullable=False)
    isbn = Column(String(20), nullable=False)
    published_date = Column(Date)
    