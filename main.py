# -*- coding: utf-8 -*-
from flask import Flask, request, abort
import json
from questions import *
import random
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return 'it\'s alive'

@app.route('/question/<int:_id>')
def question(_id):
    for q in questions:
        if q['id'] == _id:
            return json.dumps(q, ensure_ascii=False)

    abort(404)

@app.route('/question/random')
def question_random():
    return json.dumps(random.choice(questions), ensure_ascii=False)

@app.route('/question/answer/<int:_id>')
def answer(_id):
    ans = request.args.get('choice', None)
    for q in questions:
        if q['id'] == _id:
            return q['correct'] == ans

    return False

if __name__ == '__main__':
    app.run(debug=True)
