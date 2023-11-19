from model.base_model import BaseModel
from sqlalchemy import Integer, String, Column, Double


class Cart(BaseModel):
    __tablename__ = 'cart'
    item_no = Column(Integer, primary_key=True, autoincrement=True)
    session_id = Column(Integer)
    item_name = Column(String)
    quantity = Column(Integer)
    type = Column(String)
    price = Column(Double)
    img = Column(String)
    item_id = Column(Integer)

