from .__init__ import db

class TodoList(db.Model):
    """
    Table for storing the list of todo items
    """
    
    __tablename__ = "todo_list"

    list_item_id = db.Column(db.Integer, primary_key=True)

    todo_content = db.Column(db.String)
