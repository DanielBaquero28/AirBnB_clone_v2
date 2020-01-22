#!/usr/bin/python3
""" Starts a Flask web application """
from flask import Flask, render_template
from models import storage


app = Flask(__name__)


@app.teardown_appcontext
def close_session(self):
    """ Removes the current SQLAlchemy Session """
    self.storage.close()


@app.route('/states_list', strict_slashes=False)
def display_html():
    """ Displays html page within the body tag """
    return (render_template('7-states_list.html',
                            states=storage.all('State').values()))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
