from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

@app.route('/shopping-cart')
def shopping_cart():
    return 'Use Jinja templates to build out the shopping cart UI found at this route (http://127.0.0.1:5000/shopping-cart)'


if __name__ == '__main__':
    app.run()
