from sqlalchemy.orm import make_transient

from database.database_session import DatabaseSession
from model.accounts import Account
from model.book import Book


class DatabaseExecutor:
    def __init__(self):
        self._db_session = DatabaseSession()

    def get_user_accounts(self):
        with self._db_session.session() as session:
            results = session.query(Account).all()
            for result in results:
                # disconnect from database so updates aren't tracked
                session.expunge(result)
            return results

    def get_books_by_genre(self, genre):
        with self._db_session.session() as session:
            books = session.query(Book).filter_by(genre=genre).all()
            for book in books:
                # disconnect from database so updates aren't tracked
                session.expunge(book)
                make_transient(book)
            return books
