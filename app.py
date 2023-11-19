import os

from flask import Flask, render_template, request, session, redirect, url_for, jsonify
from database.database_executor import DatabaseExecutor
from model.book import Book  # Add this import
from model.accessories import Accessories  # Add this import
from werkzeug.utils import secure_filename

app = Flask(__name__)
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

# secret key for session
app.secret_key = 'TODO: Set Secret Key'

from flask import request


@app.route('/')
def home_page():
    # this would be the websites home page
    return render_template("index.html", books="pass book_data", accessories="add accessory_data")


@app.route('/add<id>', methods=['GET', 'POST'])
def add_to_cart(id):
    item = id[:1]
    book_id = int(id[1:])
    if item == "b":
        db_executor = DatabaseExecutor()
        books = db_executor.get_books_by_id(book_id)

        books_data = [{'img': book.img, 'title': book.title, 'author': book.author, 'price': book.price, 'id': book.id,
                       'genre': book.genre, 'quantity': book.quantity, 'availability': book.availability} for book in
                      books]
        book_a = books_data[0]
        db_executor.add_cart_item(1, book_a.get("title"), book_a.get("quantity"), "book", book_a.get("price"),
                                  book_a.get("img"), book_a.get("id"))
        # items = db_executor.get_cart_items()
        # for item in items:
        #  print(f'{item.item_name}')

        # db_executor.delete_cart()

        #  cart_books.append(book_a)
        template = book_a.get("genre")
        newdb_executor = DatabaseExecutor()
        nbooks = newdb_executor.get_books_by_genre(template)
        nbooks_data = [{'img': b.img, 'title': b.title, 'author': b.author, 'price': b.price, 'id': b.id,
                        'availability': b.availability} for b in
                       nbooks]
        return render_template("display-books.html", genre_page=template, books=nbooks_data)
    elif item == "a":
        db_executor = DatabaseExecutor()
        accessories = db_executor.get_accessories_by_id(book_id)
        accessory_data = [{'img': a.img, 'item_name': a.item_name, 'quantity': a.quantity, 'price': a.price,
                           'id': a.accessory_id, "availability": a.availability} for a in accessories]
        accessory_a = accessory_data[0]
        db_executor.add_cart_item(1, accessory_a.get("item_name"), accessory_a.get("quantity"), "ACCESSORY",
                                  accessory_a.get("price"), accessory_a.get("img"), accessory_a.get("id"))

        # cart_accessories.append(accessory_a)
        print("Accesory A")
        print(accessory_a)

        new_accessories = db_executor.get_accessories()
        accessories_data = [{'img': accessory.img, 'item_name': accessory.item_name, 'price': accessory.price,
                             'id': accessory.accessory_id} for accessory in new_accessories]
        return render_template("display-accessories.html", genre_page="Accessories", accessories=accessories_data)


@app.route('/display-books/<genre>', methods=['GET'])
def display_books(genre):
    db_executor = DatabaseExecutor()

    # Get books by genre
    books = db_executor.get_books_by_genre(genre)

    # Sorting parameters
    sort_by = request.args.get('sort_by', 'title')
    order = request.args.get('order', 'asc')

    # Sort the books based on the selected criteria
    if sort_by == 'title':
        books.sort(key=lambda x: x.title)
    elif sort_by == 'price':
        books.sort(key=lambda x: float(x.price))
    elif sort_by == 'quantity':
        books.sort(key=lambda x: x.quantity)

    # Handle descending order
    if order == 'desc':
        books.reverse()

    books_data = [
        {'img': book.img, 'title': book.title, 'author': book.author, 'price': book.price, 'quantity': book.quantity,
         'id': book.id} for book in books]

    return render_template("display-books.html", genre_page=genre, books=books_data, sort_by=sort_by, order=order)


# ...

@app.route('/display-accessories', methods=['GET'])
def display_accessories():
    db_executor = DatabaseExecutor()

    # Get accessories
    accessories = db_executor.get_accessories()

    # Sorting parameters
    sort_by = request.args.get('sort_by', 'title')
    order = request.args.get('order', 'asc')

    # Sort the accessories based on the selected criteria
    if sort_by == 'title':
        accessories.sort(key=lambda x: x.item_name)
    elif sort_by == 'price':
        accessories.sort(key=lambda x: float(x.price))
    elif sort_by == 'quantity':
        accessories.sort(key=lambda x: x.quantity)

    # Handle descending order
    if order == 'desc':
        accessories.reverse()

    accessories_data = [{'img': accessory.img, 'item_name': accessory.item_name, 'price': accessory.price,
                         'quantity': accessory.quantity} for accessory in accessories]

    return render_template("display-accessories.html", genre_page="Accessories", accessories=accessories_data,
                           sort_by=sort_by, order=order)


# ...

@app.route('/shopping-cart', methods=['GET', 'POST'])
def shopping_cart():
    db_executor = DatabaseExecutor()
    items = db_executor.get_cart_items()
    subtotal = 0.00

    tax = 1.08
    a_total = 0.00
    for item in items:
        print(item.item_name)
        subtotal += item.price * item.quantity
    subtotal = round(subtotal, 2)
    if request.method == 'POST':
        coupon = request.form.get('coupon')
        if str(coupon) == "COUPON":
            a_total = round(subtotal * tax, 2) - 10
            print("COUPON GOOD")
        else:
            a_total = round(subtotal * tax, 2)
    else:
        a_total = round(subtotal * tax, 2)

    return render_template("cart.html", books=items, subtotal=subtotal, tax=tax, total=a_total)


@app.route('/non-fiction')
def non_fiction():
    db_executor = DatabaseExecutor()

    # Get books by genre
    genre_page = "Non-Fiction"
    books = db_executor.get_books_by_genre(genre_page)
    books_data = [{'img': book.img, 'title': book.title, 'author': book.author, 'price': book.price, 'id': book.id} for
                  book in books]
    return render_template("display-books.html", genre_page=genre_page, books=books_data)


@app.route('/fiction')
def fiction():
    db_executor = DatabaseExecutor()

    # Get books by genre
    genre_page = "Fiction"
    books = db_executor.get_books_by_genre(genre_page)
    books_data = [{'img': book.img, 'title': book.title, 'author': book.author, 'price': book.price, 'id': book.id} for
                  book in books]
    return render_template("display-books.html", genre_page=genre_page, books=books_data)


@app.route('/romance')
def romance():
    db_executor = DatabaseExecutor()

    # Get books by genre
    genre_page = "Romance"
    books = db_executor.get_books_by_genre(genre_page)
    books_data = [{'img': book.img, 'title': book.title, 'author': book.author, 'price': book.price, 'id': book.id} for
                  book in books]
    return render_template("display-books.html", genre_page=genre_page, books=books_data)


@app.route('/action')
def action():
    db_executor = DatabaseExecutor()

    # Get books by genre
    genre_page = "Action"
    books = db_executor.get_books_by_genre(genre_page)
    books_data = [{'img': book.img, 'title': book.title, 'author': book.author, 'price': book.price, 'id': book.id} for
                  book in books]
    return render_template("display-books.html", genre_page=genre_page, books=books_data)


@app.route('/kids')
def kids():
    db_executor = DatabaseExecutor()

    # Get books by genre
    genre_page = "Kids"
    books = db_executor.get_books_by_genre(genre_page)
    books_data = [{'img': book.img, 'title': book.title, 'author': book.author, 'price': book.price, 'id': book.id} for
                  book in books]
    return render_template("display-books.html", genre_page=genre_page, books=books_data)


@app.route('/fantasy')
def fantasy():
    # Initialize the DatabaseExecutor
    db_executor = DatabaseExecutor()

    # Get books by genre
    genre_page = "Fantasy"
    books = db_executor.get_books_by_genre(genre_page)
    books_data = [{'img': book.img, 'title': book.title, 'author': book.author, 'price': book.price, 'id': book.id} for
                  book in books]
    return render_template("display-books.html", genre_page=genre_page, books=books_data)


@app.route('/horror')
def horror():
    db_executor = DatabaseExecutor()

    # Get books by genre
    genre_page = "Horror"
    books = db_executor.get_books_by_genre(genre_page)
    books_data = [{'img': book.img, 'title': book.title, 'author': book.author, 'price': book.price, 'id': book.id} for
                  book in books]
    return render_template("display-books.html", genre_page=genre_page, books=books_data)


@app.route('/comic-manga')
def comic_manga():
    db_executor = DatabaseExecutor()

    # Get books by genre
    genre_page = "Comic/Manga"
    books = db_executor.get_books_by_genre(genre_page)
    books_data = [{'img': book.img, 'title': book.title, 'author': book.author, 'price': book.price, 'id': book.id,
                   'availability': book.availability} for book in books]
    return render_template("display-books.html", genre_page=genre_page, books=books_data)


@app.route('/accessories')
def accessories():
    db_executor = DatabaseExecutor()

    # get the accessories
    genre_page = "Accessories"
    accessories = db_executor.get_accessories()
    accessories_data = [
        {'img': accessory.img, 'item_name': accessory.item_name, 'price': accessory.price, 'id': accessory.accessory_id,
         "availability": accessory.availability} for accessory in accessories]
    return render_template("display-accessories.html", genre_page="Accessories", accessories=accessories_data)


@app.route('/login', methods=['GET', 'POST'])
def login():
    db_executor = DatabaseExecutor()
    if request.method == 'POST':
        username = request.json.get('login-username')
        password = request.json.get('login-password')
        user = db_executor.authenticate_user(username, password)
        if user:
            session['username'] = username
            print("SUCCESS")
            return jsonify({"status": "success", "username": username})
        else:
            print("FAILED")
            return jsonify({"status": "failure", "error": "Invalid username or password"})


@app.route('/logout')
def logout():
    # Clear the session to log the user out
    session.pop('username', None)
    return render_template("index.html", books="pass book_data", accessories="add accessory_data")


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


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/create-item', methods=['GET', 'POST'])
def create_item():
    if request.method == 'POST':
        # Access form data and process the form submission
        item_type = request.form['item_type']
        item_name = request.form.get('item_name')
        genre = request.form.get('genre')
        title = request.form.get('title')
        author = request.form.get('author')

        # Convert the form input values to appropriate data types
        quantity = int(request.form.get('quantity_books')) if request.form.get('quantity_books') else None
        price = float(request.form.get('price_books')) if request.form.get('price_books') else None
        availability = int(request.form.get('availability_books')) if request.form.get('availability_books') else None

        # Access file data
        img_file = request.files['img']

        # Validate file type
        if img_file and allowed_file(img_file.filename):
            db_executor = DatabaseExecutor()

            # Save the image to the appropriate directory based on item type
            if item_type == 'books':
                upload_folder = os.path.join(app.root_path, 'static', 'assets', 'books')
            elif item_type == 'accessories':
                upload_folder = os.path.join(app.root_path, 'static', 'assets', 'accessories')
            else:
                return jsonify({'success': False, 'error': 'Invalid item type'})

            img_filename = secure_filename(img_file.filename)
            img_path = os.path.join(upload_folder, img_filename)
            os.makedirs(upload_folder, exist_ok=True)
            img_file.save(img_path)

            # Register the item in the database
            if item_type == 'books':
                result = db_executor.add_book(genre, title, author, quantity, price, availability, img_filename)
            elif item_type == 'accessories':
                result = db_executor.add_accessory(item_name, quantity, price, availability, img_filename)

            return jsonify(result)
        else:
            return jsonify({'success': False, 'error': 'Invalid file format'})
    else:
        # Render the form for GET requests
        return render_template('create-items.html')


@app.route('/modify-item', methods=['GET', 'POST'])
def modify_item():
    db_executor = DatabaseExecutor()
    books = db_executor.get_books()
    accessories = db_executor.get_accessories()

    return render_template('modify-items.html', books=books, accessories=accessories)


@app.route('/stock')
def display_stock():
    db_executor = DatabaseExecutor()

    # Get stock information (books and accessories)
    stock = db_executor.get_stock_information()

    # Sorting parameters
    sort_by = request.args.get('sort_by', 'title')
    order = request.args.get('order', 'asc')

    # Sort stock items based on the selected criteria
    if sort_by == 'title':
        stock.sort(
            key=lambda x: str(getattr(x, 'title', '')) if isinstance(x, Book) else str(getattr(x, 'item_name', '')))
    elif sort_by == 'price':
        stock.sort(key=lambda x: float(getattr(x, 'price', 0)))
    elif sort_by == 'quantity':
        stock.sort(key=lambda x: int(getattr(x, 'quantity', 0)))

    # Handle descending order
    if order == 'desc':
        stock.reverse()

    return render_template("stock.html", stock=stock, sort_by=sort_by, order=order)


@app.route('/orders')
def display_orders():
    db_executor = DatabaseExecutor()

    # Get stock information (books and accessories)
    stock = db_executor.get_stock_information()

    # Sorting parameters
    sort_by = request.args.get('sort_by', 'title')
    order = request.args.get('order', 'asc')

    # Sort stock items based on the selected criteria
    if sort_by == 'title':
        stock.sort(
            key=lambda x: str(getattr(x, 'title', '')) if isinstance(x, Book) else str(getattr(x, 'item_name', '')))
    elif sort_by == 'price':
        stock.sort(key=lambda x: float(getattr(x, 'price', 0)))
    elif sort_by == 'quantity':
        stock.sort(key=lambda x: int(getattr(x, 'quantity', 0)))

    # Handle descending order
    if order == 'desc':
        stock.reverse()

    return render_template("orders.html", stock=stock, sort_by=sort_by, order=order)

    return render_template("cart.html", books=items, subtotal=subtotal, tax=tax, total=a_total)


@app.route("/increase<id>")
def increase_quantity(id):
    db_executor = DatabaseExecutor()
    db_executor.increase_quantity(id)
    return redirect("/shopping-cart")


@app.route("/decrease<id>")
def decrease_quantity(id):
    db_executor = DatabaseExecutor()
    db_executor.decrease_quantity(id)
    return redirect("/shopping-cart")


@app.route('/remove-book<id>')
def remove_book(id):
    db_executor = DatabaseExecutor()
    db_executor.remove_from_cart(id)
    items = db_executor.get_cart_items()
    subtotal = 0.00
    tax = 1.08
    a_total = 0.00
    for item in items:
        subtotal += item.price
    a_total = subtotal * tax
    return render_template("cart.html", books=items, subtotal=subtotal, tax=tax, total=a_total)


@app.route("/remove-all")
def remove_books():
    db_executor = DatabaseExecutor()
    db_executor.delete_cart()
    return redirect("/shopping-cart")


@app.route('/check_login_status')
def check_login_status():
    if 'username' in session:
        return jsonify({"status": "success", "username": session['username']})
    else:
        return jsonify({"status": "failure"})


@app.route('/search', methods=["GET"])
def search():
    db_executor = DatabaseExecutor()
    user_search = request.args.get('user_search')
    item_search = user_search
    # if the item_search is a book title
    if db_executor.get_books_by_title(item_search):
        books = db_executor.get_books_by_title(item_search)
        books_data = [{'img': book.img, 'title': book.title, 'author': book.author, 'price': book.price} for book in
                      books]
        if db_executor.get_accessories_by_item_name(item_search):
            accessories = db_executor.get_accessories_by_item_name(item_search)
            accessories_data = [{'img': accessory.img, 'item_name': accessory.item_name, 'price': accessory.price} for
                                accessory in accessories]
            return render_template('search.html', user_search=user_search, books=books_data,
                                   accessories=accessories_data)
        else:
            return render_template('search.html', user_search=user_search, books=books_data)
    # if the item_search is an accessory
    elif db_executor.get_accessories_by_item_name(item_search):
        accessories = db_executor.get_accessories_by_item_name(item_search)
        accessories_data = [{'img': accessory.img, 'item_name': accessory.item_name, 'price': accessory.price} for
                            accessory in accessories]
        return render_template('search.html', user_search=user_search, accessories=accessories_data)
    # if the item is not found display all books and accessories
    else:
        books = db_executor.get_books()
        accessories = db_executor.get_accessories()
        accessories_data = [{'img': accessory.img, 'item_name': accessory.item_name, 'price': accessory.price} for
                            accessory in accessories]
        books_data = [{'img': book.img, 'title': book.title, 'author': book.author, 'price': book.price} for book in
                      books]
        return render_template('search.html', user_search=user_search + ': no results found', books=books_data,
                               accessories=accessories_data)


@app.route('/admin-create-modify')
def admin_create_modify():
    return 'figure out what to do'


if __name__ == '__main__':
    app.run(debug=True)
