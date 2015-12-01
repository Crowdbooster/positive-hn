import flask
import flask.ext.bootstrap
from uuid import uuid4
from flask import abort, request, session


import main.settings
import main.view


def current_app():
    if flask.has_app_context():
        return flask.current_app

    app = flask.Flask(__name__)
    app = _configure_app(app)
    app.app_context().push()
    return app


def _configure_app(app):
    app.config.from_object(main.settings)
    # env variable value should be a config filename for additional settings.
    app.config.from_envvar('POSITIVEHN_SETTINGS', silent=True)

    app.register_blueprint(main.view.bp, url_prefix='/')
    flask.ext.bootstrap.Bootstrap(app)

    # Add function accessible to templates.
    app.jinja_env.globals['csrf_token'] = _generate_csrf_token

    # Add a CSRF check before each request.
    @app.before_request
    def csrf_protect():
        if request.method in ['POST', 'PUT', 'DELETE']:
            token = session.pop('_csrf_token', None)
            if not token or token != request.form.get('_csrf_token'):
                abort(403)

    return app


def _generate_csrf_token():
    if '_csrf_token' not in session:
        session['_csrf_token'] = str(uuid4())
    return session['_csrf_token']
