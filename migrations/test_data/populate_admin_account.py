from model.accounts import Account
from database.database_session import DatabaseSession


class Populate:
    db: DatabaseSession = DatabaseSession()

    def add_admin_account(self, admin, username, password):
        new_account = Account(admin=admin, username=username, password=password)
        with self.db.session() as session:
            session.add(new_account)
            session.commit()


if __name__ == "__main__":
    pop = Populate()

    # Add admin account
    pop.add_admin_account(admin=True, username="admin", password="admin@123")
