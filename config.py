#!venv/bin/python
from os import environ
try:
    from urllib.parse import urlparse
except ImportError:
    from urlparse import urlparse
class Heroku(object):
    """Heroku configurations for flask."""
    def __init__(self, app=None):
        self.app = app
        if app is not None:
            self.init_app(app)
    def init_app(self, app):
    	redis_url = environ.get('REDISTOGO_URL')
        if redis_url:
            url = urlparse(redis_url)
            app.config.setdefault('REDIS_HOST', url.hostname)
            app.config.setdefault('REDIS_PORT', url.port)
            app.config.setdefault('REDIS_PASSWORD', url.password)

