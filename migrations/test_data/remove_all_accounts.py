from model.accounts import Account
from database.database_session import DatabaseSession


class Populate:
    db: DatabaseSession = DatabaseSession()

    def delete_all_accounts(self):
        with self.db.session() as session:
            session.query(Account).delete()
            session.commit()


if __name__ == "__main__":
    pop = Populate()

    pop.delete_all_accounts()
