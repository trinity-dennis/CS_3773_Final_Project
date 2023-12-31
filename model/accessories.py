from model.base_model import BaseModel
from sqlalchemy import Integer, String, Column, Float, Boolean


class Accessories(BaseModel):
    __tablename__ = 'accessories'

    accessory_id = Column(Integer, primary_key=True, autoincrement=True)
    img = Column(String)
    item_name = Column(String)
    quantity = Column(Integer)
    price = Column(Float)
    availability = Column(Integer)
    display_on_homepage = Column(Boolean)
