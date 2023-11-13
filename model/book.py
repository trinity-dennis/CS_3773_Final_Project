from model.base_model import BaseModel
from sqlalchemy import Integer, String, Column, Double


class Book(BaseModel):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True, autoincrement=True)
    genre = Column(String)
    title = Column(String)
    author = Column(String)
    price = Column(Double)
