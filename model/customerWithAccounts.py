from model.base_model import BaseModel
from sqlalchemy import Integer, String, Column, UniqueConstraint


class CustomerWithAccounts(BaseModel):
    __tablename__ = 'customer_with_accounts'

    customer_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    username = Column(String)
    password = Column(String)
    email = Column(String)
    phone_number = Column(String)
    address = Column(String)

    __table_args__ = (
        UniqueConstraint('username', 'password', 'email', 'phone_number'),
    )
