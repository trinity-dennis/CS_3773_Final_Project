from model.base_model import BaseModel
from sqlalchemy import Integer, String, Column


class UserAccount(BaseModel):
    __tablename__ = 'user_accounts'

    id = Column(Integer, primary_key=True, autoincrement=True)
    firstName = Column(String)
    lastName = Column(String)