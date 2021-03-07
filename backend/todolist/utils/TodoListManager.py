from json import dumps

from utils.dbmanagers.TodoListItemManager import TodoListItemManager
from utils.mongo_dbmanagers.TodoListResourceManager import TodoListResourceManager

class TodoListManager():
    """
    The class handles all the interactions with the TodoList Module.
    """

    def __init__(self):
        self.__todo_list_item_manager = None # for the TodoListItem Database Manager
        self.__mongodb_manager = None

    def insert_todo_item(self, db, content):
        """
        This function inserts a todo task in the database

        :params content: (string) content for the todo list item

        :returns: status (int) status code
                  response_msg (String) JSON containing message         
        """
        
        # initializing managers
        self.__todo_list_item_manager = TodoListItemManager(db)
        self.__mongodb_manager = TodoListResourceManager()

        postgres_insertion_success, list_item_id = self.__todo_list_item_manager.insert(content)

        # Make a document with the respective id in the mongodb cluster
        mongo_insertion_success = self.__mongodb_manager.insert(list_item_id, {})

        if postgres_insertion_success and mongo_insertion_success:
            status_code = 201
            response_msg = {"message": "Data Insertion successful", "list_item_id": list_item_id, "todo_content": content.todo_content}
        else:
            status_code = 500
            response_msg = {"message": "Data Insertion failed"}

        return status_code, response_msg 

    def fetch_todo_items(self, db):
        """
        The function fetches all the todo items from the database

        :returns: status (int) status code
                  response_msg (String) JSON containing message and todo_list
        """

        # initializing managers
        self.__todo_list_item_manager = TodoListItemManager(db)
        self.__mongodb_manager = TodoListResourceManager()

        status_code = 200
        response_msg = {"message": "Fetch successful!"}

        postgres_status, todo_list = self.__todo_list_item_manager.get_list()
        mongo_status, todo_list_resources = self.__mongodb_manager.list_resources()

        if not postgres_status or not mongo_status:
            status_code = 500
            response_msg = {"message": "Fetch failed!"}
            return status_code, response_msg

        mongo_result = []

        for resource in todo_list_resources:
            try:
                mongo_result.append(resource)
            except StopIteration:
                break
    
        assert len(todo_list) == len(mongo_result), "Postgres and Mongo DB are inconsistent" 

        todo_list = list(map(lambda item: {"list_item_id": item.list_item_id, "todo_content": item.todo_content}, todo_list))

        for todo_item in todo_list:
            todo_item["resources"] = next(filter(lambda item: item["_id"] == todo_item["list_item_id"], mongo_result))

        response_msg["todo_list"] = todo_list

        return status_code, response_msg

    def get_todo_item(self, db, _id):
        """
        Get a single todo item with the respective _id

        :param:     (int)   unique _id of the todo item to get
        :returns:   (dict)  todo item and all it's associated resources
        """

        # initializing managers
        self.__todo_list_item_manager = TodoListItemManager(db)
        self.__mongodb_manager = TodoListResourceManager()

        status_code = 200
        response_msg = {"message": "Fetch successful!"}

        postgres_status, todo_item = self.__todo_list_item_manager.get(_id)
        mongo_status, todo_item_resources = self.__mongodb_manager.get(_id)

        if not postgres_status or not mongo_status:
            status_code = 500
            response_msg = {"message": "Fetch failed!"}
            return status_code, response_msg

        response_msg["todo_item"] = todo_item.__dict__
        response_msg["todo_item"]["resources"] = todo_item_resources

        return status_code, response_msg
