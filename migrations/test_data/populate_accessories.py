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
         "quantity": 1, "price": 7.00, "img": "cb-calmandcool.jpg", "availability": 50},
        {"item_name": "Beaded Bookmark - You Fell Asleep Here",
         "quantity": 1, "price": 2.95, "img": "bm-youfellasleephere.jpg", "availability": 50},
        {"item_name": "Recharge Book Light, White",
         "quantity": 1, "price": 32.95, "img": "booklight.jpg", "availability": 50},
        {
            "item_name": "Lysas 4 Sets Neon Page Markers Colored Index Tabs, Fluorescent Sticky Note for Page Marker, 560pcs",
            "quantity": 1, "price": 6.49, "img": "pagemarkers.jpg", "availability": 50},

        {"item_name": "2 Pieces Dried Flower Resin Book Page Holder Transparent Thumb Ring Page Holder",
         "quantity": 1, "price": 9.95, "img": "pageholder.jpg", "availability": 50},
        {"item_name": "50pcs Book Stickers",
         "quantity": 1, "price": 7.95, "img": "bookstickers.jpg", "availability": 50},
        {"item_name": "10 Pack Bible Highlighters and Pens No Bleed, Gel Highlighter with Assorted Cute Colors",
         "quantity": 1, "price": 11.95, "img": "pen.jpg", "availability": 50},
        {"item_name": "Canvas Book Tote Bag with Pockets, Book Lovers Gifts",
         "quantity": 1, "price": 12.95, "img": "totebag.jpg", "availability": 50},
        {"item_name": "5 Rolls Highlighter Tape Transparent Marking Sticker Removable",
         "quantity": 1, "price": 6.95, "img": "roll.jpg", "availability": 50},
        {"item_name": "Adjustable Acrylic Book Stand for Reading",
         "quantity": 1, "price": 35.95, "img": "bookstand.jpg", "availability": 50},
        {"item_name": "26 Letters Personalized Hand Embroidered Corner Bookmark Cute Flower ",
         "quantity": 1, "price": 8.95, "img": "bookmark.jpg", "availability": 50},
        {"item_name": "Crochet Bookmark",
         "quantity": 1, "price": 5.95, "img": "noelbookmark.jpg", "availability": 50},
        {"item_name": "Flat Book Light for Reading in Bed at Night Clear LED",
         "quantity": 1, "price": 10.95, "img": "flatbook.jpg", "availability": 50},

    ]

    pop.insert_accessories(accessories_to_insert)
