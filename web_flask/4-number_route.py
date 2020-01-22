#!/usr/bin/python3
""" Starts a Flask web application """
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ Displays Greeting HBNB! """
    return ("Hello HBNB!")


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Displays HBNB with route /hbnb """
    return ("HBNB")


@app.route('/c/<text>', strict_slashes=False)
def hello_c(text):
    """ Diplays C and the text entered as the route """
    return ('C %s' % text.replace('_', ' '))


@app.route('/python/', defaults={'text': "is cool"})
@app.route('/python/<text>', strict_slashes=False)
def hello_python(text):
    """ Displays python and the text entered as the route or 'is cool' """
    return ('Python %s' % text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def n_number(n):
    """ Displays 'n is a number' if it is in fact one """
    return ('%d is a number' % n)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
