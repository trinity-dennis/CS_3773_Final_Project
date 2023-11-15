from model.base_model import BaseModel
from sqlalchemy import Integer, String, Column, Double


class Accessories(BaseModel):
    __tablename__ = 'accessories'

    accessory_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    description = Column(String)
    title = Column(String)
    quantity = Column(Integer)
    price = Column(Double)
