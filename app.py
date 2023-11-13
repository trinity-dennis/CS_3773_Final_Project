from flask import Flask, render_template
# from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
 
# Creating an SQLAlchemy instance
# db = SQLAlchemy(app)


#test class for books
class books:
    def __init__(self, name,author,img_name,price):
        self.name = name
        self.author = author
        self.img = img_name
        self.price = price

books_list =[]
loc = "assets/books/"
books_list.append(books("Harry Potter","JK Rowling", "harrypotter.jpg",5.00))
books_list.append(books("Game of Thrones","George R Martin ", "gameofthrones.jpg",5.00))
books_list.append(books("Lightning Thief","Rick Riordan", "lightningthief.jpg",15.00))
books_list.append(books("Shadow Of Night","Debora Harkness ", "shadowofthenight.jpg",18.81))
books_list.append(books("Enemy Tribe (Ancestors Saga Book 3)","Lori Holmes", "enemytribe.jpg",15.99))
books_list.append(books("The Ever King","L.J Andrews", "theeverking.jpg",17.99))
books_list.append(books("The Witcher Tower of Swallows ","Andrzej Sapkowski", "thewitcher.jpg",14.99))
books_list.append(books("Vows and Ruins The Legends of Thezmar","Helen Scheuerer","vowsandruins.jpg",15.99))
books_list.append(books("The Forbidden (Ancestors Saga Book 1)","Lori Holmes", "theforbidden.jpg",9.99))
books_list.append(books("Daughter of Ninmah (Ancestors Saga Book 2) ","Lori Holmes", "daughterofninmah.jpg",14.99))
books_list.append(books("The Last Kamaali (Ancestors Saga Book 4) ","Lori Holmes","thelastkamaali.jpg",15.99))

@app.route('/')
def home_page():
    # this would be the websites home page
    return render_template("index.html", genre_page="Check Out Our Vast Selection Of Books!", booksL=books_list)
    # test to see if i could route linke
    #rerenders index.html which inherits from base.html. the index.html is passed a value for the genre_page variable and shown on screen when index.html is rendered
    return render_template("index.html", genre_page="Non-Fiction")
@app.route('/fiction')
def fiction():
    # test to see if i could route linke
    return render_template("index.html", genre_page="Fiction" ,booksL=books_list)
@app.route('/romance')
def romance():
    # test to see if i could route linke
    return render_template("index.html", genre_page="Romance",booksL=books_list)

@app.route('/action')
def action():
    # test to see if i could route linke
    return render_template("index.html", genre_page="Action",booksL=books_list)

@app.route('/comedy')
def comedy():
    # test to see if i could route linke
    return render_template("index.html", genre_page="Comedy",booksL=books_list)

@app.route('/fantasy')
def fantasy():
    # test to see if i could route linke
    return render_template("index.html", genre_page="Fantasy",booksL=books_list)

@app.route('/horror')
def horror():
    # test to see if i could route linke
    return render_template("index.html", genre_page="Horror",booksL=books_list)

@app.route('/comic-manga')
def comic_manga():
    # test to see if i could route linke
    return render_template("index.html", genre_page="Comic/Manga",booksL=books_list)

@app.route('/accessories')
def accesories():
    # test to see if i could route linke
    return render_template("index.html", genre_page="Accessories")

@app.route('/shopping-cart')
def shopping_cart():
    return 'Use templates to build out the shopping cart UI found at this route (http://127.0.0.1:5000/shopping-cart)'


if __name__ == '__main__':
    app.run(debug=True)
