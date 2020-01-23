#!/usr/bin/python3
""" Starts a Flask web application """
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.teardown_appcontext
def teardown_session(exception):
    """ Removes the current SQLAlchemy Session """
    storage.close()


@app.route('/states_list', strict_slashes=False)
def display_html():
    """ Function called with /states_list route """
    states = storage.all(State)
    dic_obj = {value.id: value.name for value in states.values()}
    return render_template('7-states_list.html', items=dic_obj)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
