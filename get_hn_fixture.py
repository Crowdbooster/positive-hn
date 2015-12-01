import json
from hn import get_comments_for

with open('example_comments.json', 'w') as outfile:
    json.dump(get_comments_for('10658787'), outfile)
