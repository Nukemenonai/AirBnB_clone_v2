#!/usr/bin/python3

"""this file stes up a simple flask server """


from flask import Flask

app = Flask(__name__)


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
def python_is_cool(text="is cool", strict_slashes=False):
    """ variable rules for /python"""
    return ("Python %s" % text.replace("_", " "))

if __name__ == '__main__':
    app.run(host='0.0.0.0')
