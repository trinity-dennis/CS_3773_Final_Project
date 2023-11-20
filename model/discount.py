from model.base_model import BaseModel
from sqlalchemy import Column, String, Float, Integer

class Discount(BaseModel):
    __tablename__ = 'discounts'

    id = Column(Integer, primary_key=True, autoincrement=True)
    code = Column(String, unique=True, nullable=False)
    percentage = Column(Float, nullable=False)

    def __init__(self, code, percentage):
        self.code = code
        self.percentage = percentage
