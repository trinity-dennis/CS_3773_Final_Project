from model.base_model import BaseModel
from sqlalchemy import Integer, String, Column, Boolean


class Account(BaseModel):
    __tablename__ = 'accounts'

    id = Column(Integer, primary_key=True, autoincrement=True)
    admin = Column(Boolean)
    username = Column(String)
    password = Column(String)