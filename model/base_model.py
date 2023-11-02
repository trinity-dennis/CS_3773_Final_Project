from database.database_session import DatabaseSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session

Base = declarative_base()


class BaseModel(Base):
    __abstract__ = True

    def save(self) -> None:
        with DatabaseSession().session() as session:
            session.add(self)

    def delete(self) -> None:
        with DatabaseSession().session() as session:
            session.delete(self)

    @classmethod
    def query(cls):
        with DatabaseSession().session() as session:
            session.query(cls)
