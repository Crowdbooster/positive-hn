import flask

bp = flask.Blueprint('view', __name__, template_folder='templates')


@bp.route('/')
def index():
    return flask.render_template('index.html')
