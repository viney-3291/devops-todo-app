from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory storage
tasks = []
next_id = 1

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

@app.route('/tasks', methods=['POST'])
def add_task():
    global next_id
    data = request.get_json()
    task = {
        'id': next_id,
        'title': data['title'],
        'done': False
    }
    tasks.append(task)
    next_id += 1
    return jsonify(task), 201

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    global tasks
    tasks = [t for t in tasks if t['id'] != task_id]
    return jsonify({'message': 'deleted'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)