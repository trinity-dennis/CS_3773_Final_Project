from flask import Flask, render_template, request
from database.database_executor import DatabaseExecutor

app = Flask(__name__)


@app.route('/')
def home_page():
    # this would be the websites home page
    return render_template("index.html", books="pass book_data", accessories="add accessory_data")


@app.route('/non-fiction')
def non_fiction():
    db_executor = DatabaseExecutor()

    # Get books by genre
    genre_page = "Non-Fiction"
    books = db_executor.get_books_by_genre(genre_page)
    books_data = [{'img': book.img, 'title': book.title, 'author': book.author, 'price': book.price} for book in books]
    return render_template("display-books.html", genre_page=genre_page, books=books_data)


@app.route('/fiction')
def fiction():
    db_executor = DatabaseExecutor()

    # Get books by genre
    genre_page = "Fiction"
    books = db_executor.get_books_by_genre(genre_page)
    books_data = [{'img': book.img, 'title': book.title, 'author': book.author, 'price': book.price} for book in books]
    return render_template("display-books.html", genre_page=genre_page, books=books_data)


@app.route('/romance')
def romance():
    db_executor = DatabaseExecutor()

    # Get books by genre
    genre_page = "Romance"
    books = db_executor.get_books_by_genre(genre_page)
    books_data = [{'img': book.img, 'title': book.title, 'author': book.author, 'price': book.price} for book in books]
    return render_template("display-books.html", genre_page=genre_page, books=books_data)


@app.route('/action')
def action():
    db_executor = DatabaseExecutor()

    # Get books by genre
    genre_page = "Action"
    books = db_executor.get_books_by_genre(genre_page)
    books_data = [{'img': book.img, 'title': book.title, 'author': book.author, 'price': book.price} for book in books]
    return render_template("display-books.html", genre_page=genre_page, books=books_data)


@app.route('/kids')
def kids():
    db_executor = DatabaseExecutor()

    # Get books by genre
    genre_page = "Kids"
    books = db_executor.get_books_by_genre(genre_page)
    books_data = [{'img': book.img, 'title': book.title, 'author': book.author, 'price': book.price} for book in books]
    return render_template("display-books.html", genre_page=genre_page, books=books_data)


@app.route('/fantasy')
def fantasy():
    # Initialize the DatabaseExecutor
    db_executor = DatabaseExecutor()

    # Get books by genre
    genre_page = "Fantasy"
    books = db_executor.get_books_by_genre(genre_page)
    books_data = [{'img': book.img, 'title': book.title, 'author': book.author, 'price': book.price} for book in books]
    return render_template("display-books.html", genre_page=genre_page, books=books_data)


@app.route('/horror')
def horror():
    db_executor = DatabaseExecutor()
    
    # Get books by genre
    genre_page = "Horror"
    books = db_executor.get_books_by_genre(genre_page)
    books_data = [{'img': book.img, 'title': book.title, 'author': book.author, 'price': book.price} for book in books]
    return render_template("display-books.html", genre_page=genre_page, books=books_data)


@app.route('/comic-manga')
def comic_manga():
    db_executor = DatabaseExecutor()

    # Get books by genre
    genre_page = "Comic/Manga"
    books = db_executor.get_books_by_genre(genre_page)
    books_data = [{'img': book.img, 'title': book.title, 'author': book.author, 'price': book.price} for book in books]
    return render_template("display-books.html",  genre_page=genre_page, books=books_data)


@app.route('/accessories')
def accesories():
    db_executor = DatabaseExecutor()

    # get the accessories
    genre_page = "Accessories"
    accessories = db_executor.get_accessories()
    accessories_data = [{'img': accessory.img, 'item_name': accessory.item_name, 'price': accessory.price} for accessory in accessories]
    return render_template("display-accessories.html", genre_page="Accessories", accessories=accessories_data)

@app.route('/login', methods=['GET', 'POST'])
def login():
    db_executor = DatabaseExecutor()
    if request.method == 'POST':
        username = request.json.get('login-username')
        password = request.json.get('login-password')
        user = db_executor.authenticate_user(username, password)
        if user:
            print("SUCCESS")
            return 'success'
        else:
            print("FAILED")
            return 'Invalid username or password'

@app.route('/signup', methods=['POST'])
def signup():
    db_executor = DatabaseExecutor()
    if request.method == 'POST':
        # will automatically set admin to false, since we should never be creating an admin account through the website
        admin = False
        username = request.json.get('signup-username')
        password = request.json.get('signup-password')

        # register the user
        db_executor.register_user(admin, username, password)

        # return empty string to complete valid response (can change later to pop up a success message)
        return ''


@app.route('/shopping-cart')
def shopping_cart():
    return 'Use templates to build out the shopping cart UI found at this route (http://127.0.0.1:5000/shopping-cart)'


if __name__ == '__main__':
    app.run(debug=True)
