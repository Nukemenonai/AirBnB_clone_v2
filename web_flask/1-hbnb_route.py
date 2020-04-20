#!/usr/bin/python3

"""this file stes up a simple flask server """


from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_route(strict_slashes=False):
    return ("Hello HBNB!")

@app.route('/hbnb')
def hbnb_route(strict_slashes=False):
    return ("HBNB")
