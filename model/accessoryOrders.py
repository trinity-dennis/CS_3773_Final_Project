from model.base_model import BaseModel
from sqlalchemy import Integer, Column, Double, ForeignKey
from sqlalchemy.orm import relationship


class AccessoryOrders(BaseModel):
    __tablename__ = 'accessory_orders'

    accessory_order_id = Column(Integer, primary_key=True, autoincrement=True)
    accessory_id = Column(Integer, ForeignKey('accessories.accessory_id'))
    guest_id = Column(Integer, ForeignKey('customer_without_accounts.guest_id'))
    customer_id = Column(Integer, ForeignKey('customer_with_accounts.customer_id'))
    quantity = Column(Integer)
    order_total = Column(Double)

    accessory = relationship('Accessory')
