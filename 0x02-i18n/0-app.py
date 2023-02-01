#!/usr/bin/env python3
"""Basic flask app  """
from flask import Flask, render_template
from templates import *
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def root():
    """ Homepage URL """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port='5000')
