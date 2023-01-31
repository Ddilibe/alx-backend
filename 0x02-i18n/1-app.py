#!/usr/bin/env python3
""" Script to run a Flask Server """
from flask import Flask, render_template
from flask_babel import Babel


class Config():
    """ Class for Flask configuration """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route('/', strict_slashes=False)
def index() -> render_template:
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(port='5000', host='0.0.0.0', debug=True)
