#!/usr/bin/python3

"""this file stes up a simple flask server """


from flask import Flask, escape, render_template
from models import storage, State


app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def list_of_states():
    """ This method returns the list of states stored in storage engine"""
    states = sorted(storage.all(State).values(), key=lambda k: k.name)
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def close(self=None):
    """ closes the session  """
    storage.close()


if __name__ == "__main__":
    """ running the app  """
    app.run(host='0.0.0.0', port='5000')
