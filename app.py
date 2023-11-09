from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home_page():
    # this would be the websites home page
    return render_template("index.html", genre_page="Check Out Our Vast Selection Of Books!")
@app.route('/non-fiction')
def non_fiction():
    # test to see if i could route linke
    #rerenders index.html which inherits from base.html. the index.html is passed a value for the genre_page variable and shown on screen when index.html is rendered
    return render_template("index.html", genre_page="Non-Fiction")
@app.route('/fiction')
def fiction():
    # test to see if i could route linke
    return render_template("index.html", genre_page="Fiction")
@app.route('/romance')
def romance():
    # test to see if i could route linke
    return render_template("index.html", genre_page="Romance")

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
    # test to see if i could route linke
    return render_template("index.html", genre_page="Fantasy")

@app.route('/horror')
def horror():
    # test to see if i could route linke
    return render_template("index.html", genre_page="Horror")

@app.route('/comic-manga')
def comic_manga():
    # test to see if i could route linke
    return render_template("index.html", genre_page="Comic/Manga")

@app.route('/accessories')
def accesories():
    # test to see if i could route linke
    return render_template("index.html", genre_page="Accessories")

@app.route('/shopping-cart')
def shopping_cart():
    return 'Use templates to build out the shopping cart UI found at this route (http://127.0.0.1:5000/shopping-cart)'


if __name__ == '__main__':
    app.run(debug=True)
