#!/usr/bin/python3

"""this file stes up a simple flask server """


from flask import Flask, escape, render_template
from models.state import State
from models import storage

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states_and_state(id=None):
    """ """
    status = 0
    states = sorted(storage.all(State).values(), key=lambda k: k.name)
    state = ""
    cities = []

    for el in states:
        if id == el.id:
           state = el
           status = 1
           break

    status = (2 if id is not None and status == 0 else 0)
    if status == 1:
        cities = sorted(state.cities, key=lambda k: k.name)
        state = state.name

    return render_template('9-states.html',
                           state=state,
                           states=states,
                           cities=cities,
                           status=status)

@app.teardown_appcontext
def close(res_or_exc):
    """ closes the session  """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
