#!/usr/bin/python3

"""this file stes up a simple flask server """


from flask import Flask, escape, render_template
from models import storage
from models import State

app = Flask(__name__)
app.url_map.strict_slashes = False

@app.route('/')
def hello_route(strict_slashes=False):
    """ route for default page """
    return ("Hello HBNB!")


@app.route('/hbnb')
def hbnb_route(strict_slashes=False):
    """ route for /hbnb """
    return ("HBNB")


@app.route('/c/<string:text>')
def c_is_fun(text, strict_slashes=False):
    return ("C %s" % text.replace("_", " "))


@app.route('/python/<string:text>')
@app.route('/python/')
@app.route('/python')
def python_is_cool(text='is cool', strict_slashes=False):
    """ variable rules for /python"""
    return ("Python %s" % escape(text.replace("_", " ")))


@app.route('/number/<int:number>')
def is_it_a_number(number, strict_slashes=False):
    """ rules for number variables routing"""
    return ("%d is a number" % number)


@app.route('/number_template/<int:number>')
def number_template(number, strict_slashes=False):
    """ displays an html template on a valid number"""
    return render_template('5-number.html', number=number)


@app.route('/number_odd_or_even/<int:number>')
def odd_or_even(number, strict_slashes=False):
    """ displays even or odd depending on the number given """
    return render_template(
        '6-number_odd_or_even.html',
        number=number,
        evenodd=("even" if number % 2 == 0 else "odd"))


@app.route('/states_list')
def list_of_states():
    """ This method returns the list of states stored in storage engine"""
    states = storage.all(State)
    sorted_states = []
    for state in states:
        sorted_states.append([states[state].id, states[state].name])
    sorted_states.sort()
    return render_template('7-states_list.html', data=sorted_states)


@app.teardown_appcontext
def close(self=None):
    """ closes the session  """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
