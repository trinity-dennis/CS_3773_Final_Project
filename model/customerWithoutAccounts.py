from model.base_model import BaseModel
from sqlalchemy import Integer, String, Column


class CustomerWithoutAccounts(BaseModel):
    __tablename__ = 'customer_without_accounts'

    guest_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    phone_number = Column(String)
    email = Column(String)
    address = Column(String)
