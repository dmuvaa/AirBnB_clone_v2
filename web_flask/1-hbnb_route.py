#!/usr/bin/python3

"""imports a module"""


from flask import Flask


@app.route('/', strict_slashes=False)
def hello():
    """Return Hello and Route"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Hbnb Route"""
    return "HBNB"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
