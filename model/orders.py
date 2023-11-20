from model.base_model import BaseModel
from sqlalchemy import Integer, Column, ForeignKey, Text, Float
from sqlalchemy.orm import relationship
from model.book import Book  # Add this import
from model.accounts import Account  # Adjust the import based on your actual module structure
from model.accessories import Accessories

class Orders(BaseModel):
    __tablename__ = 'orders'

    order_id = Column(Integer, primary_key=True, autoincrement=True)
    book_id = Column(Integer, ForeignKey('books.id'))
    accessory_id = Column(Integer, ForeignKey('accessories.accessory_id'))
    customer_id = Column(Integer, ForeignKey('accounts.id'))
    order_date = Column(Text)
    order_total = Column(Float)

    book = relationship('Book')
    accessory = relationship('Accessories')
    customer = relationship('Account')  # Assuming 'Account' is the model for customers

