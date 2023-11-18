from model.accounts import Account
from database.database_session import DatabaseSession


class Populate:
    db: DatabaseSession = DatabaseSession()

    def delete_all_except_admin(self):
         with self.db.session() as session:
            # deletes all accounts that are not admin
            session.query(Account).filter(Account.id != 1).delete()
            session.commit()


if __name__ == "__main__":
    pop = Populate()
    pop.delete_all_except_admin()
