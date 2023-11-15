from model.base_model import BaseModel
from sqlalchemy import Integer, Column, String, Double, ForeignKey, Text
from sqlalchemy.orm import relationship


class Orders(BaseModel):
    __tablename__ = 'orders'

    order_id = Column(Integer, primary_key=True, autoincrement=True)
    book_id = Column(Integer, ForeignKey('books.id'))
    accessory_id = Column(Integer, ForeignKey('accessories.accessory_id'))
    customer_id = Column(Integer, ForeignKey('user_accounts.id'))
    order_date = Column(Text)
    order_total = Column(Double)

    book = relationship('Book')
    accessory = relationship('Accessory')
