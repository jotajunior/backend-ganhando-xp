from flask import Flask, request, abort
import json
from questions import *
import random

app = Flask(__name__)


@app.route('/')
def index():
    return 'it\'s alive'

@app.route('/question/<int:_id>')
def question(_id):
    for q in questions:
        if q['id'] == _id:
            return json.dumps(q)

    abort(404)

@app.route('/question/random')
def question_random():
    return json.dumps(random.choice(questions))

@app.route('/question/answer/<int:_id>')
def answer(_id):
    ans = request.args.get('choice', None)
    for q in questions:
        if q['id'] == _id:
            return q['correct'] == ans

    return False

if __name__ == '__main__':
    app.run(debug=True)
