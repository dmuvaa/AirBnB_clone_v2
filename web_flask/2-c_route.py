#!/usr/bin/python3

"""imports a module"""


from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Return Hello and Route"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Hbnb Route"""
    return "HBNB"

@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """text to replace '_' and '.'"""
    return "C " + text.replace('_', ' ')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)