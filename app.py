from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data to store tasks
tasks = []

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

@app.route('/tasks', methods=['POST'])
def add_task():
    data = request.get_json()
    if 'task' in data:
        new_task = {'task': data['task']}
        tasks.append(new_task)
        return jsonify(new_task), 201
    else:
        return jsonify({'error': 'Task field is required'}), 400

if __name__ == '__main__':
    app.run(debug=True)
