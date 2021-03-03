from typing import List, Optional, Dict

from pydantic import BaseModel

class TodoBase(BaseModel):
    todo_content: Optional[str]

class TodoCreate(TodoBase):
    pass

class Todo(TodoBase):
    list_item_id: Optional[int]
    message: str

    class Config:
        orm_mode = True

class TodoFetch(BaseModel):
    message: str
    todo_list: Optional[List[Dict[str, str]]]

    class Config:
        orm_mode = True