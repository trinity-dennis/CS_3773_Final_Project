from flask import Flask, render_template, request, session, redirect, url_for, jsonify
import random

from database.database_executor import DatabaseExecutor

app = Flask(__name__)
cart_books =[]
cart_accessories = []


# secret key for session
app.secret_key = 'TODO: Set Secret Key'

@app.route('/')
def home_page():
    # this would be the websites home page
    return render_template("index.html", books="pass book_data", accessories="add accessory_data")

@app.route('/add<id>',methods=['GET', 'POST'])
def add_to_cart(id):
    item = id[:1]
    book_id = int(id[1:])
    if item == "b":
        db_executor = DatabaseExecutor()
        books = db_executor.get_books_by_id(book_id)

        books_data = [{'img': book.img, 'title': book.title, 'author': book.author, 'price': book.price, 'id': book.id,
                       'genre': book.genre, 'quantity': book.quantity, 'availability': book.availability} for book in books]
        book_a = books_data[0]
        db_executor.add_cart_item(1,book_a.get("title"), book_a.get("quantity"), "book", book_a.get("price"),book_a.get("img"), book_a.get("id"))
        #items = db_executor.get_cart_items()
        #for item in items:
          #  print(f'{item.item_name}')

        #db_executor.delete_cart()

      #  cart_books.append(book_a)
        template = book_a.get("genre")
        newdb_executor = DatabaseExecutor()
        nbooks = newdb_executor.get_books_by_genre(template)
        nbooks_data = [{'img': b.img, 'title': b.title, 'author': b.author, 'price': b.price, 'id': b.id, 'availability': b.availability} for b in
                       nbooks]
        return render_template("display-books.html", genre_page=template, books=nbooks_data)
    elif item =="a":
        db_executor = DatabaseExecutor()
        accessories = db_executor.get_accessories_by_id(book_id)
        accessory_data = [{'img': a.img, 'item_name': a.item_name, 'quantity': a.quantity, 'price': a.price,
                           'id': a.accessory_id, "availability": a.availability} for a in accessories]
        accessory_a = accessory_data[0]
        db_executor.add_cart_item(1 , accessory_a.get("item_name"), accessory_a.get("quantity"),"ACCESSORY", accessory_a.get("price"),accessory_a.get("img"), accessory_a.get("id"))

        #cart_accessories.append(accessory_a)
        print("Accesory A")
        print(accessory_a)

        new_accessories = db_executor.get_accessories()
        accessories_data = [{'img': accessory.img, 'item_name': accessory.item_name, 'price': accessory.price,
                             'id': accessory.accessory_id} for accessory in new_accessories]
        return render_template("display-accessories.html", genre_page="Accessories", accessories=accessories_data)







@app.route('/non-fiction')
def non_fiction():
    db_executor = DatabaseExecutor()

    # Get books by genre
    genre_page = "Non-Fiction"
    books = db_executor.get_books_by_genre(genre_page)
    books_data = [{'img': book.img, 'title': book.title, 'author': book.author, 'price': book.price, 'id': book.id,
                   'availability': book.availability } for book in books]
    return render_template("display-books.html", genre_page=genre_page, books=books_data)


@app.route('/fiction')
def fiction():
    db_executor = DatabaseExecutor()

    # Get books by genre
    genre_page = "Fiction"
    books = db_executor.get_books_by_genre(genre_page)
    books_data = [{'img': book.img, 'title': book.title, 'author': book.author, 'price': book.price ,'id': book.id,'availability': book.availability } for book in books]
    return render_template("display-books.html", genre_page=genre_page, books=books_data)


@app.route('/romance')
def romance():
    db_executor = DatabaseExecutor()

    # Get books by genre
    genre_page = "Romance"
    books = db_executor.get_books_by_genre(genre_page)
    books_data = [{'img': book.img, 'title': book.title, 'author': book.author, 'price': book.price , 'id': book.id, 'availability': book.availability } for book in books]
    return render_template("display-books.html", genre_page=genre_page, books=books_data)


@app.route('/action')
def action():
    db_executor = DatabaseExecutor()

    # Get books by genre
    genre_page = "Action"
    books = db_executor.get_books_by_genre(genre_page)
    books_data = [{'img': book.img, 'title': book.title, 'author': book.author, 'price': book.price, 'id': book.id ,'availability': book.availability } for book in books]
    return render_template("display-books.html", genre_page=genre_page, books=books_data)


@app.route('/kids')
def kids():
    db_executor = DatabaseExecutor()

    # Get books by genre
    genre_page = "Kids"
    books = db_executor.get_books_by_genre(genre_page)
    books_data = [{'img': book.img, 'title': book.title, 'author': book.author, 'price': book.price, 'id': book.id ,'availability': book.availability} for book in books]
    return render_template("display-books.html", genre_page=genre_page, books=books_data)


@app.route('/fantasy')
def fantasy():
    # Initialize the DatabaseExecutor
    db_executor = DatabaseExecutor()

    # Get books by genre
    genre_page = "Fantasy"
    books = db_executor.get_books_by_genre(genre_page)
    books_data = [{'img': book.img, 'title': book.title, 'author': book.author, 'price': book.price ,'id': book.id, 'availability': book.availability } for book in books]
    return render_template("display-books.html", genre_page=genre_page, books=books_data)


@app.route('/horror')
def horror():
    db_executor = DatabaseExecutor()
    
    # Get books by genre
    genre_page = "Horror"
    books = db_executor.get_books_by_genre(genre_page)
    books_data = [{'img': book.img, 'title': book.title, 'author': book.author, 'price': book.price ,'id': book.id ,'availability': book.availability} for book in books]
    return render_template("display-books.html", genre_page=genre_page, books=books_data)


@app.route('/comic-manga')
def comic_manga():
    db_executor = DatabaseExecutor()

    # Get books by genre
    genre_page = "Comic/Manga"
    books = db_executor.get_books_by_genre(genre_page)
    books_data = [{'img': book.img, 'title': book.title, 'author': book.author, 'price': book.price ,'id': book.id ,'availability': book.availability} for book in books]
    return render_template("display-books.html",  genre_page=genre_page, books=books_data)


@app.route('/accessories')
def accesories():
    db_executor = DatabaseExecutor()

    # get the accessories
    genre_page = "Accessories"
    accessories = db_executor.get_accessories()
    accessories_data = [{'img': accessory.img, 'item_name': accessory.item_name, 'price': accessory.price, 'id': accessory.accessory_id, "availability": accessory.availability} for accessory in accessories]
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
            session['session_id'] = random.random()
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


@app.route('/shopping-cart')
def shopping_cart():
    db_executor = DatabaseExecutor()
    items = db_executor.get_cart_items()
    subtotal = 0.00
    tax = 1.08
    a_total =0.00
    for item in items:
        subtotal += item.price * item.quantity
    subtotal = round(subtotal,2)
    a_total = round(subtotal * tax , 2)


    return render_template("cart.html", books=items, subtotal=subtotal, tax=tax, total=a_total)
@app.route("/increase<id>")
def increase_quantity(id):
    db_executor= DatabaseExecutor()
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
    return render_template("cart.html", books=items,subtotal=subtotal,tax=tax,total=a_total)

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


if __name__ == '__main__':
    app.run(debug=True)
