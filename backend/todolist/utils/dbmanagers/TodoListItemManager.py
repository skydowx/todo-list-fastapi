from flask import current_app as app

from app.models import db, TodoList

class TodoListItemManager():
    """
    This class handles all the database interactions, via ORM, related to the todo_list table
    """

    def __init__(self):
        pass

    def insert(self, content):
        """
        Inserts data into the table. 

        :params content: (str) description of the todo task

        :returns: (boolean) True/False depending on the success of insertion
        """

        success = True

        data_rec = TodoList()
        data_rec.todo_content = content

        db.session.add(data_rec)

        try:
            db.session.commit()
        
        except Exception as e:
            db.session.rollback()
            db.session.flush()
            app.logger.debug("Exception: {}".format(e))

            return not success
        
        return success

    def get_todo_list(self):
        """
        Fetches all entries in the todo_list table.

        :returns: (boolean) True/False depending on the result of the query
                  (list) todo list item
        """

        success = True

        try:
            items = TodoList.query.all()
        except Exception as e:
            app.logger.debug("Exception: {}".format(e))
            return not success, []

        return True, items