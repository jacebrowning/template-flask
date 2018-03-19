from urllib.parse import urlencode, unquote
from pathlib import Path

from flask import url_for, current_app, request
from flask_api import FlaskAPI
import log

from . import api
from . import views
from . import extensions


def create_app(config):
    app = FlaskAPI(__name__)
    app.config.from_object(config)

    configure_logging(app)

    register_blueprints(app)
    register_extensions(app)

    enable_cache_busting(app)

    return app


def configure_logging(app):
    if app.config['DEBUG']:
        level = log.DEBUG
        pattern = "%(levelname)s: %(name)s:%(lineno)d: %(message)s"
    else:
        level = log.INFO
        pattern = "%(levelname)s: %(message)s"
    log.init(level=level, format=pattern)

    def log_request(response=None):
        if current_app.debug:
            path = request.path
            if request.args:
                path += "?%s" % unquote(urlencode(request.args))
            if response:
                log.info("%s: %s - %i", request.method, path,
                         response.status_code)
            else:
                log.info("%s: %s", request.method, path)

        return response

    log.silence('werkzeug', allow_warning=True)
    app.before_request(log_request)
    app.after_request(log_request)


def register_blueprints(app):
    register_backend(app)
    register_frontend(app)


def register_backend(app):
    app.register_blueprint(api.root.blueprint)


def register_frontend(app):
    app.register_blueprint(views.index.blueprint)


def register_extensions(app):
    extensions.bootstrap.init_app(app)


def enable_cache_busting(app):

    def dated_url_for(endpoint, **values):
        if endpoint == 'static':
            filename = values.get('filename', None)
            if filename:
                path = Path(app.root_path, endpoint, filename)
                values['q'] = int(path.stat().st_mtime)
        return url_for(endpoint, **values)

    app.context_processor(lambda: dict(url_for=dated_url_for))
