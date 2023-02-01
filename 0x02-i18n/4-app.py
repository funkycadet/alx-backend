#!/usr/bin/env python3
""" Basic flask app that configures Babel """
from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """ config class """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """ get_locale method to set locale language
    from available languages """
    data = request.query_string.decode('utf-8').split('&')
    data_table = dict(map(
        lambda i: (i if '=' in i else '{}='.format(i)).split('='),
        data
    ))
    if 'locale' in data_table:
        if data_table['locale'] in app.config["LANGUAGES"]:
            return data_table['locale']
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def root():
    """ Homepage URL """
    return render_template(('3-index.html'))


if __name__ == '__main__':
    app.run(host='127.0.0.1', port='5000')
