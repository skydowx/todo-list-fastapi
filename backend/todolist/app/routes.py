"""Application routes"""

from flask import current_app as app, Response
from flask import request, jsonify

from utils.TodoListManager import TodoListManager

@app.route('/insertListItem', methods=['POST'])
def insert_list_item():
    try: 
        content = request.get_json()['content']
    except KeyError:
        message = "insertListItem expects a string in the content key only"
        return Response(message, status=500)

    todo_content = content

    status, message = TodoListManager().insert_list_item(todo_content)

    return Response(message, status=status)

@app.route('/fetchListItems', methods=['GET'])
def fetch_list_items():
    status, message = TodoListManager().fetch_todo_items()
    return Response(message, status=status)