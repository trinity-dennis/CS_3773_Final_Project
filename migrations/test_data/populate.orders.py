from model.orders import Orders
from database.database_session import DatabaseSession


class PopulateOrders:
    db: DatabaseSession = DatabaseSession()

    def delete_all_orders(self):
        with self.db.session() as session:
            session.query(Orders).delete()
            session.commit()


if __name__ == "__main__":
    pop = PopulateOrders()
    pop.delete_all_orders()
