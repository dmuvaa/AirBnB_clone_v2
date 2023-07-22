#!/usr/bin/python3

"""imports a module."""

from flask import Flask


app = Flask(__name__)


def hello():
    """
    return hello
    """
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
