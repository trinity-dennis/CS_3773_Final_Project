from model.base_model import BaseModel
from sqlalchemy import Integer, String, Column, Double


class Accessories(BaseModel):
    __tablename__ = 'accessories'

    accessory_id = Column(Integer, primary_key=True, autoincrement=True)
    img = Column(String)
    item_name = Column(String)
    quantity = Column(Integer)
    price = Column(Double)
    availability = Column(Integer)