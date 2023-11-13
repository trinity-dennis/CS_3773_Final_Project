from model.user_account import UserAccount
from database.database_session import DatabaseSession


class Populate:
    db: DatabaseSession = DatabaseSession()

    def insert_user_accounts(self):
        with self.db.session() as session:
            ua = UserAccount(id=1, firstName="Billy", lastName="Bob")
            session.add(ua)
            session.commit()


if __name__ == "__main__":
    pop = Populate()
    pop.insert_user_accounts()
