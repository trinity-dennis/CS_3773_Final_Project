
from model.base_model import BaseModel
from sqlalchemy import Integer, Column, String, Double, ForeignKey, Text
from sqlalchemy.orm import relationship
from model.book import Book
from model.accounts import Account
from model.accessories import Accessories


class Orders(BaseModel):
    __tablename__ = 'orders'

    order_id = Column(Integer, primary_key=True, autoincrement=True)
    book_id = Column(Integer, ForeignKey('books.id'))
    accessory_id = Column(Integer, ForeignKey('accessories.accessory_id'))
    customer_id = Column(Integer, ForeignKey('accounts.id'))
    order_date = Column(Text)
    order_total = Column(Double)

    book = relationship('Book')
    accessory = relationship('Accessories')
    customer = relationship('Account')
