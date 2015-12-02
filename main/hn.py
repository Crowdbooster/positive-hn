import requests
import json
import os

CURR_DIR = os.path.dirname(os.path.abspath(__file__))
FIXTURE_PATH = os.path.join(CURR_DIR, 'example_comments.json')

ITEM_ENDPOINT_URL = 'https://hacker-news.firebaseio.com/v0/item/{}.json'


def get_item_from_hn(item_id):
    return requests.get(ITEM_ENDPOINT_URL.format(item_id)).json()


def get_comments_for(item_id):
    data = get_item_from_hn(item_id)
    kids = data.get('kids', [])

    # Get all the child comments in a flat list with reduce.
    return reduce(lambda flat_comments, kid_ids: flat_comments + get_comments_recursive(kid_ids),
                  kids,
                  [])


def get_comments_recursive(item_id):
    data = get_item_from_hn(item_id)

    if data.get('type', None) == 'comment' and not data.get('deleted', False):
        kids = data.get('kids', [])

        # Get the child comments recursively. The reduce function concatenates them to
        # a flat list instead of having a nested hierarchy.
        return reduce(lambda flat_comments, kid_ids: flat_comments + get_comments_recursive(kid_ids),
                      kids,  # loop through all the kids of this comment
                      [data.get('text')])  # Init reduce with the current comment text
    return []


def load_example_comments():
    return json.load(open(FIXTURE_PATH, 'r'))
