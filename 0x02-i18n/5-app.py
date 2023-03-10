#!/usr/bin/env python3
""" Basic flask app that configures Babel """
from flask import Flask, render_template, request, g
from flask_babel import Babel
from typing import Union, Dict


class Config:
    """ config class """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    """ get_user method
    Retrieves a user based on id
    """
    login_user = request.args.get('login_as', None)
    if login_user != None and int(login_user) in users.keys():
        return users.get(int(login_user))
    return None


@app.before_request
def before_request():
    """ before request function
    Function to perform some routines before each endpoints
    """
    user = get_user()
    g.user = user


@babel.localeselector
def get_locale():
    """
    Set locale language from available languages
    """
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def root():
    """ Homepage URL """
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port='5000')
