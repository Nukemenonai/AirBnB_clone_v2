#!/usr/bin/python3

"""this file stes up a simple flask server """


from flask import Flask, escape, render_template
from models.state import State
from models import storage

app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_state():
    """ """
    states = storage.all(State).values()
    states = sorted(states, key=lambda k: k.name)
    cbs = []
    for state in states:
        cbs.append([state, sorted(state.cities, key=lambda k: k.name)])
    return render_template('8-cities_by_states.html', data=cbs)


@app.teardown_appcontext
def close(res_or_exc):
    """ closes the session  """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
