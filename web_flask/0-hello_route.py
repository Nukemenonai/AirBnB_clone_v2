#!/usr/bin/python3

"""this file stes up a simple flask server """


from flask import Flask


app = Flask(__name__)


@app.route('/')
def hello_route(strict_slashes=False):
    """ this handles routing for /  """
    return ("Hello HBNB!")

if __name__ == '__main__':
    app.run(host='0.0.0.0')
