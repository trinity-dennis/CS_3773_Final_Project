from model.book import Book
from database.database_session import DatabaseSession


class Populate:
    db: DatabaseSession = DatabaseSession()

    def delete_all_books(self):
        with self.db.session() as session:
            session.query(Book).delete()
            session.commit()

    def insert_books(self, books):
        # Delete all existing books before inserting new ones
        self.delete_all_books()

        with self.db.session() as session:
            for book_data in books:
                book = Book(**book_data)
                session.add(book)

            # Commit the changes
            session.commit()


if __name__ == "__main__":
    pop = Populate()

    # list of books
    books_to_insert = [
        {"genre": "Fantasy", "title": "Harry Potter", "author": "JK Rowling", "price": 5.00, "img": "harrypotter.jpg"},
        {"genre": "Fantasy", "title": "Game of Thrones", "author": "George R Martin", "price": 5.00, "img": "gameofthrones.jpg"},
        {"genre": "Fantasy", "title": "Lightning Thief", "author": "Rick Riordan", "price": 15.00, "img": "lightningthief.jpg"},
        {"genre": "Fantasy", "title": "Shadow of Night", "author": "Debora Harkness", "price": 18.81, "img": "shadowofthenight.jpg"},
        {"genre": "Fantasy", "title": "Enemy Tribe (Ancestors Saga Book 3)", "author": "Lori Holmes",
         "price": 15.99, "img": "enemytribe.jpg"},
        {"genre": "Fantasy", "title": "The Ever King", "author": "L.J Andrews", "price": 17.99, "img": "theeverking.jpg"},
        {"genre": "Fantasy", "title": "The Witcher Tower of Swallows", "author": "Andrzej Sapkowski",
         "price": 14.99, "img": "thewitcher.jpg"},
        {"genre": "Fantasy", "title": "Vows and Ruins The Legends of Thezmar", "author": "Helen Scheuerer",
         "price": 15.99, "img": "vowsandruins.jpg"},
        {"genre": "Fantasy", "title": "The Forbidden (Ancestors Saga Book 1)", "author": "Lori Holmes",
         "price": 9.99, "img": "theforbidden.jpg"},
        {"genre": "Fantasy", "title": "Daughter of Ninmah (Ancestors Saga Book 2)", "author": "Lori Holmes",
         "price": 14.99, "img": "daughterofninmah.jpg"},
        {"genre": "Fantasy", "title": "The Last Kamaali (Ancestors Saga Book 4)", "author": "Lori Holmes",
         "price": 15.99, "img": "thelastkamaali.jpg"}
    ]

    pop.insert_books(books_to_insert)
