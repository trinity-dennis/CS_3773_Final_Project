from model.discount import Discount
from database.database_session import DatabaseSession

class PopulateCodes:
    db: DatabaseSession = DatabaseSession()

    def delete_all_discounts(self):
        with self.db.session() as session:
            session.query(Discount).delete()
            session.commit()

    def insert_discounts(self, discounts):
        # Delete all existing discounts before inserting new ones
        self.delete_all_discounts()

        with self.db.session() as session:
            for discount_data in discounts:
                discount = Discount(**discount_data)
                session.add(discount)

            # Commit the changes
            session.commit()

if __name__ == "__main__":
    pop_codes = PopulateCodes()

    # List of discount codes
    discounts_to_insert = [
        {"code": "CODE1", "percentage": 10.0},
        {"code": "CODE2", "percentage": 15.0},
        {"code": "CODE3", "percentage": 20.0},
        # Add more discount codes as needed
    ]

    pop_codes.insert_discounts(discounts_to_insert)
