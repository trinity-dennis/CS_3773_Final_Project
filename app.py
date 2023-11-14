from flask import Flask, render_template
from database.database_executor import DatabaseExecutor

app = Flask(__name__)


@app.route('/')
def home_page():
    # this would be the websites home page
    return render_template("index.html", genre_page="Check Out Our Vast Selection Of Books!")


@app.route('/non-fiction')
def non_fiction():
    db_executor = DatabaseExecutor()

    # Get books by genre
    genre_page = "Non-Fiction"
    books = db_executor.get_books_by_genre(genre_page)
    books_data = [{'img': book.img, 'title': book.title, 'author': book.author, 'price': book.price} for book in books]
    return render_template("index.html", genre_page=genre_page, books=books_data)


@app.route('/fiction')
def fiction():
    # test to see if i could route linke
    return render_template("index.html", genre_page="Fiction")


@app.route('/romance')
def romance():
    db_executor = DatabaseExecutor()

    # Get books by genre
    genre_page = "Romance"
    books = db_executor.get_books_by_genre(genre_page)
    books_data = [{'img': book.img, 'title': book.title, 'author': book.author, 'price': book.price} for book in books]
    return render_template("index.html", genre_page=genre_page, books=books_data)


@app.route('/action')
def action():
    # test to see if i could route linke
    return render_template("index.html", genre_page="Action")


@app.route('/comedy')
def comedy():
    # test to see if i could route linke
    return render_template("index.html", genre_page="Comedy")


@app.route('/fantasy')
def fantasy():
    # Initialize the DatabaseExecutor
    db_executor = DatabaseExecutor()

    # Get books by genre
    genre_page = "Fantasy"
    books = db_executor.get_books_by_genre(genre_page)
    books_data = [{'img': book.img, 'title': book.title, 'author': book.author, 'price': book.price} for book in books]
    return render_template("index.html", genre_page=genre_page, books=books_data)


@app.route('/horror')
def horror():
    db_executor = DatabaseExecutor()
    
    # Get books by genre
    genre_page = "Horror"
    books = db_executor.get_books_by_genre(genre_page)
    books_data = [{'img': book.img, 'title': book.title, 'author': book.author, 'price': book.price} for book in books]
    return render_template("index.html", genre_page=genre_page, books=books_data)


@app.route('/comic-manga')
def comic_manga():
    db_executor = DatabaseExecutor()

    # Get books by genre
    genre_page = "Comic/Manga"
    books = db_executor.get_books_by_genre(genre_page)
    books_data = [{'img': book.img, 'title': book.title, 'author': book.author, 'price': book.price} for book in books]
    return render_template("index.html",  genre_page=genre_page, books=books_data)


@app.route('/accessories')
def accesories():
    # test to see if i could route linke
    return render_template("index.html", genre_page="Accessories")


@app.route('/shopping-cart')
def shopping_cart():
    return 'Use templates to build out the shopping cart UI found at this route (http://127.0.0.1:5000/shopping-cart)'


if __name__ == '__main__':
    app.run(debug=True)
