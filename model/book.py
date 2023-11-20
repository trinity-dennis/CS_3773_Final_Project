from model.base_model import BaseModel
from sqlalchemy import Integer, String, Column, Float, Boolean


class Book(BaseModel):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True, autoincrement=True)
    img = Column(String)
    genre = Column(String)
    title = Column(String)
    author = Column(String)
    quantity = Column(Integer)
    price = Column(Float)
    availability = Column(Integer)
    display_on_homepage = Column(Boolean)
