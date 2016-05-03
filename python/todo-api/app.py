#!flask/bin/python3

from flask import Flask, jsonify
from flask import make_response
from flask import request
from flask import abort

app = Flask(__name__)

tasks = [
    {
        'id' : 1,
        'title': u'Buy groceries',
        'desription': u'Milk,stuff',
        'done': False
    }
    ,
    {
        'id' : 2,
        'title': u'Buy groceries',
        'desription': u'Milk,stuff',
        'done': False
    }
]

@app.route('/')
def index():
    return "hello, internet"

@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    return jsonify({'task':task[0]})


@app.route('/todo/api/v1.0/tasks', methods=['POST'])
def create_task():
    if not request.json or not 'title' in request.json:
        abort(400)
    task = {
        'id': tasks[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'done': False
    }
    tasks.append(task)
    return jsonify({'task': task}), 201

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == "__main__":
    app.run(debug=True)
