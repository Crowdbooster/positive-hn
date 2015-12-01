import requests
import json


TEXT_PROCESSING_URL = 'https://japerk-text-processing.p.mashape.com'
MASHAPE_KEY = 'NVyd4vXI5mmshGwFGKvcS5zER7jtp1RqOZejsnVqmBOSojwQN2'


# text-processing api calls w/ standardized headers
def call_sentiment_api(endpoint, data):
    headers = {
        'X-Mashape-Key': MASHAPE_KEY,
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    url = TEXT_PROCESSING_URL + endpoint
    return requests.post(url, headers=headers, data=data)

""" Sentiment Scoring """
def get_neg_score(text):
    res = call_sentiment_api('/sentiment/', {'text': text})

    classified_text = {
        'text': text,
        'label': None,
        'sentiment': {}
    }
    if res.status_code == 200:
        data = json.loads(res.text)
        classified_text['label'] = data['label']
        classified_text['sentiment'] = data['probability']

    return classified_text

def sort_by_neg(texts):
    return sorted(texts, key=lambda t: t['sentiment']['neg'], reverse=True)

def sort_and_score(comments):
    classified_comments = [get_neg_score(c) for c in comments]
    return sort_by_neg(classified_comments)

""" POS Tagging """
def get_pos_tags(text):
    data = {
        'language': 'english',
        'output': 'tagged',
        'text': text,
    }
    res = call_sentiment_api('/tag/', data)

    tagged_text = {
        'tagged': False,
        'text': text
    }
    # print res.text
    if res.status_code == 200:
        data = json.loads(res.text)
        tagged_text['tagged'] = True
        tagged_text['text'] = data['text']

    return tagged_text

def replace_neg_adj(tagged_text): # TODO
    pass

def transform_to_pos(comment): # TODO
    pass


