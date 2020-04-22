#!/usr/bin/python3

"""this file stes up a simple flask server """


from flask import Flask, escape, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states_list')
def list_of_states(strict_slashes=False):
    """ This method returns the list of states stored in storage engine"""
    States = storage.all(State)
    sorted_states = []
    for state in States:
        sorted_states.append([States[state].id, States[state].name])
    sorted_states.sort()
    return render_template('7-states_list.html', states=sorted_states)


@app.teardown_appcontext
def handle_teardown(self=None):
    """ closes the session  """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
