from sqlalchemy.orm import make_transient

from database.database_session import DatabaseSession
from model.accounts import Account
from model.book import Book
from model.accessories import Accessories


class DatabaseExecutor:
    def __init__(self):
        self._db_session = DatabaseSession()

    def register_user(self, username, password):
        new_user = Account(username=username, password=password)
        with self._db_session.session() as session:
            session.add(new_user)

    def get_books_by_genre(self, genre):
        with self._db_session.session() as session:
            books = session.query(Book).filter_by(genre=genre).all()
            for book in books:
                # disconnect from database so updates aren't tracked
                session.expunge(book)
                make_transient(book)
            return books

    def get_accessories(self):
        with self._db_session.session() as session:
            accessories = session.query(Accessories).all()
            for accessory in accessories:
                # disconnect from database so updates aren't tracked
                session.expunge(accessory)
                make_transient(accessory)
            return accessories
