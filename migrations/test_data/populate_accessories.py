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

        {"item_name": "2 Pieces Dried Flower Resin Book Page Holder Transparent Thumb Ring Page Holder",
         "quantity": 25, "price": 9.95, "img": "pageholder.jpg"},
        {"item_name": "50pcs Book Stickers",
         "quantity": 25, "price": 7.95, "img": "bookstickers.jpg"},
        {"item_name": "10 Pack Bible Highlighters and Pens No Bleed, Gel Highlighter with Assorted Cute Colors",
         "quantity": 25, "price": 11.95, "img": "pen.jpg"},
        {"item_name": "Canvas Book Tote Bag with Pockets, Book Lovers Gifts",
         "quantity": 25, "price": 12.95, "img": "totebag.jpg"},
        {"item_name": "5 Rolls Highlighter Tape Transparent Marking Sticker Removable",
         "quantity": 25, "price": 6.95, "img": "roll.jpg"},
        {"item_name": "Adjustable Acrylic Book Stand for Reading",
         "quantity": 25, "price": 35.95, "img": "bookstand.jpg"},
        {"item_name": "26 Letters Personalized Hand Embroidered Corner Bookmark Cute Flower ",
         "quantity": 25, "price": 8.95, "img": "bookmark.jpg"},
        {"item_name": "Crochet Bookmark",
         "quantity": 25, "price": 5.95, "img": "noelbookmark.jpg"},
        {"item_name": "Flat Book Light for Reading in Bed at Night Clear LED",
         "quantity": 25, "price": 10.95, "img": "flatbook.jpg"},

    ]

    pop.insert_accessories(accessories_to_insert)
