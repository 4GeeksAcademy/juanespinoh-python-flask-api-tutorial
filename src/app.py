from flask import Flask,jsonify,request

app=Flask(__name__)

todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]

@app.route('/myroute', methods=['GET'])
def hello_world():
    return 'Hello World!'

@app.route('/todos', methods=['GET'])
def todos_controller():
    result = jsonify(todos)
    print(result)
    return result

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body=request.json
    todos.append({"done":request_body.get("done"), "label":request_body.get("label")})
    print(todos)
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    todos.pop(position)
    print("This is the position to delete:", position)
    return jsonify(todos)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)