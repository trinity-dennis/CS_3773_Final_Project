from model.orders import Orders
from database.database_session import DatabaseSession
from model.base_model import BaseModel
from sqlalchemy import Integer, Column, ForeignKey, Text, Float
from sqlalchemy.orm import relationship
from model.book import Book  # Add this import
from model.accessories import Accessories

class PopulateOrders:
    db: DatabaseSession = DatabaseSession()

    def delete_all_orders(self):
        with self.db.session() as session:
            session.query(Orders).delete()
            session.commit()

    def insert_orders(self, orders):
        # Delete all existing orders before inserting new ones
        self.delete_all_orders()

        with self.db.session() as session:
            for order_data in orders:
                order = Orders(**order_data)
                session.add(order)

            # Commit the changes
            session.commit()

if __name__ == "__main__":
    pop_orders = PopulateOrders()

    # List of orders
    orders_to_insert = [
        {"book_id": 1, "accessory_id": 1, "customer_id": 1, "order_date": "2023-11-20", "order_total": 10.95},
        {"book_id": 2, "accessory_id": 2, "customer_id": 2, "order_date": "2023-11-21", "order_total": 15.95},
        {"book_id": 3, "accessory_id": 3, "customer_id": 3, "order_date": "2023-11-22", "order_total": 20.95},
        # Add more orders as needed
    ]

    pop_orders.insert_orders(orders_to_insert)
