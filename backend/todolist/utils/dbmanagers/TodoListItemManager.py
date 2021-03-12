from app.models import TodoList

class TodoListItemManager():
    """
    This class handles all the database interactions, via ORM, related to the todo_list table
    """

    def __init__(self, db):
        self.__db_request_session = db

    def insert(self, content):
        """
        Inserts data into the table. 

        :params content: (str) description of the todo task

        :returns: (boolean) True/False depending on the success of insertion
        """

        success = True

        data_rec = TodoList()
        data_rec.todo_content = content.todo_content

        self.__db_request_session.add(data_rec)

        try:
            self.__db_request_session.commit()
            self.__db_request_session.refresh(data_rec)
        
        except Exception as e:
            self.__db_request_session.rollback()
            self.__db_request_session.flush()
            # app.logger.debug("Exception: {}".format(e))

            return not success, None

        return success, data_rec.list_item_id

    def get(self, _id):
        """
        Retrieve a single todolist item by it's id
        
        :param _id: (int) unique id of a todolist item
        :returns:   (boolean) True/False based on retrieval success
                    (dict)    Record that was retrieved
        """

        success = True

        try:
            item = self.__db_request_session.query(TodoList).get(_id)
        except Exception as e:
            # app.logger.debug("Exception: {}".format(e))
            return not success, None

        return True, item
        
        

    def get_list(self):
        """
        Fetches all entries in the todo_list table.

        :returns: (boolean) True/False depending on the result of the query
                  (list) todo list item
        """

        success = True

        try:
            items = self.__db_request_session.query(TodoList).all()
        except Exception as e:
            # app.logger.debug("Exception: {}".format(e))
            return not success, []

        return True, items