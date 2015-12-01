#!/usr/bin/env python

import flask_failsafe
import flask.ext.script


@flask_failsafe.failsafe
def current_app():
    import main.app
    return main.app.current_app()


manager = flask.ext.script.Manager(current_app)


@manager.shell
def shell_context():
    return {'app': current_app()}


if __name__ == '__main__':
    manager.run()
