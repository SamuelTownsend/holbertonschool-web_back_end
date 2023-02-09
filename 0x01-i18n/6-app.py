#!/usr/bin/env python3
''' Flask app '''


from flask import Flask, g, render_template, request
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config(object):
    ''' Config class '''
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


def get_user():
    ''' Retrieves user '''
    userId = request.args.get('login_as')
    try:
        return users.get(int(userId))
    except Exception:
        return None


@app.before_request
def before_request():
    ''' Functions to run before request '''
    g.user = get_user()


@babel.localeselector
def get_locale():
    ''' Locale selector '''
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale
    try:
        if g.user and g.user['locale']\
             and g.user['locale'] in app.config['LANGUAGES']:
            return g.user['locale']
    except Exception:
        return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    ''' Index page '''
    return render_template('6-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
