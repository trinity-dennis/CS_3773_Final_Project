from model.base_model import BaseModel
from sqlalchemy import Integer, Column, Double, ForeignKey
from sqlalchemy.orm import relationship


class BookOrders(BaseModel):
    __tablename__ = 'book_orders'

    book_order_id = Column(Integer, primary_key=True, autoincrement=True)
    book_id = Column(Integer, ForeignKey('books.id'))
    guest_id = Column(Integer, ForeignKey('customer_without_accounts.guest_id'))
    customer_id = Column(Integer, ForeignKey('customer_with_accounts.customer_id'))
    quantity = Column(Integer)
    order_total = Column(Double)

    book = relationship('Book')
