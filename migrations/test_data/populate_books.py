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
         "price": 27.00, "img": "thewager.jpg"},
        {"genre": "Horror", "title": "The Shining", "author": "Stephen King",
         "price": 29.99, "img": "Shining.jpg"},
        {"genre": "Horror", "title": "Dracula", "author": "Bram Stoker",
         "price": 15.99, "img": "Dracula.jpg"},
        {"genre": "Horror", "title": "Frankenstein", "author": "Mary Shelly",
         "price": 14.99, "img": "Frankenstein.jpg"},
        {"genre": "Horror", "title": "IT", "author": "Stephen King",
         "price": 25.99, "img": "IT.jpg"},
        {"genre": "Horror", "title": "The Haunting of Hill House", "author": "Shirley Jackson",
         "price": 10.99, "img": "HauntingOfHillHouse.jpg"},
        {"genre": "Horror", "title": "Psycho", "author": "Robert Bloch",
         "price": 22.99, "img": "Psycho.jpg"},
        {"genre": "Horror", "title": "The Silence of the Lambs", "author": "Thomas Harris",
         "price": 12.99, "img": "SilenceOfTheLambs.jpg"},
        {"genre": "Horror", "title": "Carrie", "author": "Stephen King",
         "price": 19.99, "img": "Carrie.jpg"},
        {"genre": "Horror", "title": "American Psycho", "author": "Bret Easton Ellis",
         "price": 34.99, "img": "AmericanPsycho.jpg"},
        {"genre": "Horror", "title": "The Girl with All the Gifts", "author": "M.R. Carey",
         "price": 5.99, "img": "TheGirlWithAllTheGifts.jpg"},
        {"genre": "Horror", "title": "The Girl Next Door", "author": "Jack Ketchum",
         "price": 12.99, "img": "TheGirlNextDoor.jpg"},
        {"genre": "Horror", "title": "The Ring", "author": "Koji Suzuki",
         "price": 8.99, "img": "Ring.jpg"},
        {"genre": "Horror", "title": "The Amityville Horror", "author": "Jay Anson",
         "price": 21.99, "img": "TheAmityvilleHorror.jpg"},
        {"genre": "Horror", "title": "Bird Box", "author": "Josh Malerman",
         "price": 39.99, "img": "BirdBox.jpg"},
        {"genre": "Horror", "title": "World War Z", "author": "Max Brooks",
         "price": 32.99, "img": "WorldWarZ.jpg"},
        {"genre": "Horror", "title": "Heart-Shaped Box", "author": "Joe Hill",
         "price": 11.99, "img": "HeartShapedBox.jpg"},
        {"genre": "Horror", "title": "House of Leaves", "author": "Mark Z. Danielewski",
         "price": 7.99, "img": "HouseOfLeaves"},
        {"genre": "Horror", "title": "The Exorcist", "author": "William Peter Blatty",
         "price": 35.99, "img": "TheExorcist.jpg"},
        {"genre": "Horror", "title": "The Cabin at the End of the World", "author": "Paul Tremblay",
         "price": 17.99, "img": "TheCabinAtTheEndOfTheWorld.jpg"},
        {"genre": "Horror", "title": "The Terror", "author": "Dan Simmons",
         "price": 24.99, "img": "TheTerror.jpg"}
    ]

    pop.insert_books(books_to_insert)
