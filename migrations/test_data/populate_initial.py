from model.accounts import Account
from database.database_session import DatabaseSession


class Populate:
    db: DatabaseSession = DatabaseSession()

    # def insert_user_accounts(self):
    #     with self.db.session() as session:
    #         ua = Account(id=1, username="Billy", password="Bob")
    #         session.add(ua)
    #         session.commit()


if __name__ == "__main__":
    pop = Populate()
    # pop.insert_user_accounts()
