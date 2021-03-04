from sqlalchemy import Boolean, Column, ForeignKey, Integer, String

from app.config import Base

class TodoList(Base):
    """
    Table for storing the list of todo items
    """
    
    __tablename__ = "todo_list"

    list_item_id = Column(Integer, primary_key=True)

    todo_content = Column(String(512))