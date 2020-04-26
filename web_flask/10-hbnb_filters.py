#!/usr/bin/python3

"""this file stes up a simple flask server """


from flask import Flask, escape, render_template
from models.state import State
from models.city import City
from models.amenity import Amenity
from models import storage

app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
@app.route('/hbnb_filter/<string:id>')
def hbnb_filters():
    """ display a developed  index html """
    status = 0
    states = sorted(storage.all(State).values(), key=lambda k: k.name)
    amenities = sorted(storage.all(Amenity).values(), key=lambda k: k.name)
    state = ""
    cities = sorted(state.cities, key=lambda k: k.name)

    for el in states:
        if id == el.id:
            state = el
            status = 1
            break

    if status == 1:
        cities = sorted(state.cities, key=lambda k: k.name)
        state = state.name
    else:
        status = (2 if id is not None else 0)

    return render_template('10-hbnb_filters.html', states=states, amenities=amenities)


@app.teardown_appcontext
def close(res_or_exc):
    """ closes the session  """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
