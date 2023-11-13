from model.book import Book
from database.database_session import DatabaseSession


class Populate:
    db: DatabaseSession = DatabaseSession()

    def insert_books(self, books):
        with self.db.session() as session:
            for book_data in books:
                book = Book(**book_data)
                session.add(book)
            session.commit()


if __name__ == "__main__":
    pop = Populate()

    # list of books
    books_to_insert = [
        {"id": 1, "genre": "Fantasy", "title": "Harry Potter", "author": "JK Rowling", "price": 5.00},
        {"id": 2, "genre": "Fantasy", "title": "Game of Thrones", "author": "George R Martin", "price": 5.00},
        {"id": 3, "genre": "Fantasy", "title": "Lightning Thief", "author": "Rick Riordan", "price": 15.00},
        {"id": 4, "genre": "Fantasy", "title": "Shadow of Night", "author": "Debora Harkness", "price": 18.81},
        {"id": 5, "genre": "Fantasy", "title": "Enemy Tribe (Ancestors Saga Book 3)", "author": "Lori Holmes",
         "price": 15.99},
        {"id": 6, "genre": "Fantasy", "title": "The Ever King", "author": "L.J Andrews", "price": 17.99},
        {"id": 7, "genre": "Fantasy", "title": "The Witcher Tower of Swallows", "author": "Andrzej Sapkowski",
         "price": 14.99},
        {"id": 8, "genre": "Fantasy", "title": "Vows and Ruins The Legends of Thezmar", "author": "Helen Scheuerer",
         "price": 15.99},
        {"id": 9, "genre": "Fantasy", "title": "The Forbidden (Ancestors Saga Book 1)", "author": "Lori Holmes",
         "price": 9.99},
        {"id": 10, "genre": "Fantasy", "title": "Daughter of Ninmah (Ancestors Saga Book 2)", "author": "Lori Holmes",
         "price": 14.99},
        {"id": 11, "genre": "Fantasy", "title": "The Last Kamaali (Ancestors Saga Book 4)", "author": "Lori Holmes",
         "price": 15.99}
    ]

    pop.insert_books(books_to_insert)