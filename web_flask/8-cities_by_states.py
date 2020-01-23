#!/usr/bin/python3
""" Starts a Flask web application """
from flask import Flask, render_template
from models import storage


app = Flask(__name__)


@app.teardown_appcontext
def teardown_session(self):
    """ Removes the current SQLAlchemy Session """
    storage.close()


@app.route('/states_list', strict_slashes=False)
def display_html():
    """ Function called with /states_list route """
    return render_template('8-cities_by_states.html',
                           states=storage.all('State').values())

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
