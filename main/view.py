import flask

from hn import get_comments_for, load_example_comments
from sentiment import sort_and_score

bp = flask.Blueprint('view', __name__, template_folder='templates')


@bp.route('/')
def index():
    return flask.render_template('index.html')


@bp.route('api.json')
def api():
    example_comments = load_example_comments()
    scored_comments = sort_and_score(example_comments)
    return (flask.jsonify(posts=scored_comments), 200)
