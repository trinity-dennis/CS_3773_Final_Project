from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    # this would be the websites home page
    return render_template("index.html")

@app.route('/shopping-cart')
def shopping_cart():
    return 'Use templates to build out the shopping cart UI found at this route (http://127.0.0.1:5000/shopping-cart)'


if __name__ == '__main__':
    app.run()
