from database.database_session import DatabaseSession
from model.user_account import UserAccount


class DatabaseExecutor:
    def __init__(self):
        self._db_session = DatabaseSession()

    def get_user_accounts(self):
        with self._db_session.session() as session:
            results = session.query(UserAccount).all()
            for result in results:
                # disconnect from database so updates aren't tracked
                session.expunge(result)
            return results
