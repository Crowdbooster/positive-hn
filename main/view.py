import flask

bp = flask.Blueprint('view', __name__, template_folder='templates')


@bp.route('/')
def index():
    return flask.render_template('index.html')


@bp.route('api.json')
def api():
    hardcoded_posts = [
        {'text': 'a post', 'sentiment': 0.5},
        {'text': 'another post', 'sentiment': 0.8},
    ]
    return (flask.jsonify(posts=hardcoded_posts), 200)
