#!/usr/bin/python3

"""this file stes up a simple flask server """


from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_route(strict_slashes=False):
    """ routing /  """
    return ("Hello HBNB!")


@app.route('/hbnb')
def hbnb_route(strict_slashes=False):
    """ routing for /hbnb """
    return ("HBNB")

if __name__ == '__main__':
    app.run(host='0.0.0.0')
