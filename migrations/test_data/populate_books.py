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
        {"genre": "Fantasy", "title": "Game of Thrones", "author": "George R Martin", "price": 5.00,
         "img": "gameofthrones.jpg"},
        {"genre": "Fantasy", "title": "Lightning Thief", "author": "Rick Riordan", "price": 15.00,
         "img": "lightningthief.jpg"},
        {"genre": "Fantasy", "title": "Shadow of Night", "author": "Debora Harkness", "price": 18.81,
         "img": "shadowofthenight.jpg"},
        {"genre": "Fantasy", "title": "Enemy Tribe (Ancestors Saga Book 3)", "author": "Lori Holmes",
         "price": 15.99, "img": "enemytribe.jpg"},
        {"genre": "Fantasy", "title": "The Ever King", "author": "L.J Andrews", "price": 17.99,
         "img": "theeverking.jpg"},
        {"genre": "Fantasy", "title": "The Witcher Tower of Swallows", "author": "Andrzej Sapkowski",
         "price": 14.99, "img": "thewitcher.jpg"},
        {"genre": "Fantasy", "title": "Vows and Ruins The Legends of Thezmar", "author": "Helen Scheuerer",
         "price": 15.99, "img": "vowsandruins.jpg"},
        {"genre": "Fantasy", "title": "The Forbidden (Ancestors Saga Book 1)", "author": "Lori Holmes",
         "price": 9.99, "img": "theforbidden.jpg"},
        {"genre": "Fantasy", "title": "Daughter of Ninmah (Ancestors Saga Book 2)", "author": "Lori Holmes",
         "price": 14.99, "img": "daughterofninmah.jpg"},
        {"genre": "Fantasy", "title": "The Last Kamaali (Ancestors Saga Book 4)", "author": "Lori Holmes",
         "price": 15.99, "img": "thelastkamaali.jpg"},
        {"genre": "Fantasy", "title": "A Study in Drowning", "author": "Ava Reid",
         "price": 17.99, "img": "astudyindrowning.jpg"},
        {"genre": "Non-Fiction", "title": "American Demon: Eliot Ness and the Hunt for America's Jack the Ripper",
         "author": "Daniel Stashower", "price": 20.00, "img": "americandemon.jpg"},
        {"genre": "Non-Fiction", "title": "Atomic Habits: An Easy & Proven Way to Build Good Habits & Break Bad Ones",
         "author": "James Clear", "price": 22.99, "img": "atomichabits.jpg"},
        {"genre": "Non-Fiction", "title": "Be Useful: Seven Tools for Life", "author": "Arnold Schwarzenegger",
         "price": 23.80, "img": "beuseful.jpg"},
        {"genre": "Non-Fiction", "title": "Blood on Their Hands: Murder, Corruption, and the Fall of the Murdaugh Dynasty",
         "author": "Mandy Matney", "price": 26.09, "img": "bloodontheirhands.jpg"},
        {"genre": "Non-Fiction", "title": "BraveTart: Iconic American Desserts",
         "author": "Stella Parks, J. Kenji López-Alt (Foreword by)", "price": 31.49, "img": "bravetart.jpg"},
        {"genre": "Non-Fiction", "title": "Elvis and Me: The True Story of the Love Between Priscilla Presley and the King of Rock N' Roll",
         "author": "Priscilla Beaulieu Presley, Sandra Harmon", "price": 20.00, "img": "elvisandme.jpg"},
        {"genre": "Non-Fiction", "title": "Ghosts of Honolulu: A Japanese Spy, a Japanese American Spy Hunter, and the Untold Story of Pearl Harbor",
         "author": "Mark Harmon, Leon Carroll (With)", "price": 26.99, "img": "ghostsofhonolulu.jpg"},
        {"genre": "Non-Fiction", "title": "How to Know a Person: The Art of Seeing Others Deeply and Being Deeply Seen",
         "author": "David Brooks", "price": 25.50, "img": "howtoknowaperson.jpg"},
        {"genre": "Non-Fiction", "title": "Seceding from Secession: The Civil War, Politics, and the Creation of West Virginia",
         "author": "Eric J. Wittenberg, Edmund A. Sargus Jr., Penny L. Barrick", "price": 32.95, "img": "secedingfromsecession.jpg"},
        {"genre": "Non-Fiction", "title": "The Creative Act: A Way of Being", "author": "Rick Rubin", "price": 27.99,
         "img": "thecreativeact.jpg"},
        {"genre": "Non-Fiction", "title": "The Fund: Ray Dalio, Bridgewater Associates, and the Unraveling of a Wall Street Legend",
         "author": "Rob Copeland", "price": 28.80, "img": "thefund.jpg"},
        {"genre": "Non-Fiction", "title": "The Wager: A Tale of Shipwreck, Mutiny and Murder", "author": "David Grann",
         "price": 27.00, "img": "thewager.jpg"}
    ]

    pop.insert_books(books_to_insert)
