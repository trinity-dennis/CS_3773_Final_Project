from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    # this would be the websites home page
    return render_template("index.html", genre_page="Check Out Our Vast Selection Of Books!")
@app.route('/Non-Fiction')
def non_fiction():  # put application's code here
    # test to see if i could route linke
    #rerenders index.html which inherits from base.html. the index.html is passed a value for the genre_page variable and shown on screen when index.html is rendered
    return render_template("index.html", genre_page="Check Out Our Non Fiction!")
@app.route('/Fiction')
def fiction():  # put application's code here
    # test to see if i could route linke
    return render_template("index.html", genre_page="Check Out Our Fiction")
@app.route('/Romance')
def romance():  # put application's code here
    # test to see if i could route linke
    return render_template("index.html", genre_page="Check Out Our  Romance")

@app.route('/shopping-cart')
def shopping_cart():
    return 'Use templates to build out the shopping cart UI found at this route (http://127.0.0.1:5000/shopping-cart)'


if __name__ == '__main__':
    app.run(debug=True)
