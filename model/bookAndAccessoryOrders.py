from model.base_model import BaseModel
from sqlalchemy import Integer, Column, String, Double, ForeignKey, Text
from sqlalchemy.orm import relationship


class BookAndAccessoryOrders(BaseModel):
    __tablename__ = 'book_and_accessory_orders'

    order_id = Column(Integer, primary_key=True, autoincrement=True)
    book_id = Column(Integer, ForeignKey('books.id'))
    accessory_id = Column(Integer, ForeignKey('accessories.accessory_id'))
    guest_id = Column(Integer, ForeignKey('customer_without_accounts.guest_id'))
    customer_id = Column(Integer, ForeignKey('customer_with_accounts.customer_id'))
    order_date = Column(Text)
    order_total = Column(Double)

    book = relationship('Book')
    accessory = relationship('Accessory')
