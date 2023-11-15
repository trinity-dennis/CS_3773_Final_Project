from model.accessories import Accessories
from database.database_session import DatabaseSession


class Populate:
    db: DatabaseSession = DatabaseSession()

    def delete_all_accessories(self):
        with self.db.session() as session:
            session.query(Accessories).delete()
            session.commit()

    def insert_accessories(self, accessories):
        # Delete all existing books before inserting new ones
        self.delete_all_accessories()

        with self.db.session() as session:
            for accessory_data in accessories:
                accessory = Accessories(**accessory_data)
                session.add(accessory)

            # Commit the changes
            session.commit()


if __name__ == "__main__":
    pop = Populate()

    # list of books
    accessories_to_insert = [
        {"item_name": "Be Calm and Color: Channel Your Anxiety into a Soothing, Creative Activity",
         "quantity": 25, "price": 7.00, "img": "cb-calmandcool.jpg"},
        {"item_name": "Beaded Bookmark - You Fell Asleep Here",
         "quantity": 25, "price": 2.95, "img": "bm-youfellasleephere.jpg"},
        {"item_name": "Recharge Book Light, White",
         "quantity": 25, "price": 32.95, "img": "booklight.jpg"},
        {"item_name": "Lysas 4 Sets Neon Page Markers Colored Index Tabs, Fluorescent Sticky Note for Page Marker, 560pcs",
         "quantity": 25, "price": 6.49, "img": "pagemarkers.jpg"},
    ]

    pop.insert_accessories(accessories_to_insert)
