#!/usr/bin/python3
""" Starts a Flask web application """
from flask import Flask, render_template
from models import storage


app = Flask(__name__)


@app.teardown_appcontext
def teardown_session(self):
    storage.close()


@app.route('/states')
@app.route('/states/<id>')
def display_html_page(id=None):
    if id is not None:
        id = 'State.' +id
    return render_template(
        '9-states.html', states=storage.all("State"), state_id=id)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
