from json import dumps

from flask import current_app as app

from utils.dbmanagers.TodoListItemManager import TodoListItemManager

class TodoListManager():
    """
    The class handles all the interactions with the TodoList Module.
    """

    def __init__(self):
        self.__todo_list_item_manager = None # for the TodoListItem Database Manager

    def insert_list_item(self, content):
        """
        This function inserts a todo task in the database

        :params content: (string) content for the todo list item

        :returns: status (int) status code
                  response_msg (String) JSON containing message         
        """
        
        # initializing managers
        self.__todo_list_item_manager = TodoListItemManager()

        insertion_success = self.__todo_list_item_manager.insert(content)

        if insertion_success:
            status_code = 201
            response_msg = {"message": "A new todo item has been added to the database."}
        else:
            status_code = 500
            response_msg = {"message": "Data Insertion failed"}

        return status_code, dumps(response_msg) 

    def fetch_todo_items(self):
        """
        The function fetches all the todo items from the database

        :returns: status (int) status code
                  response_msg (String) JSON containing message and todo_list
        """

        # initializing managers
        self.__todo_list_item_manager = TodoListItemManager()

        status_code = 200
        response_msg = {"message": "Fetch successful!"}

        status, todo_list = self.__todo_list_item_manager.get_todo_list()
        
        if not status:
            status_code = 500
            response_msg = {"message": "Fetch failed!"}
            return status_code, dumps(response_msg)

        todo_list = list(map(lambda item: {"list_item_id": item.list_item_id, "content": item.todo_content}, todo_list))

        response_msg["todo_list"] = todo_list

        return status_code, dumps(response_msg)
