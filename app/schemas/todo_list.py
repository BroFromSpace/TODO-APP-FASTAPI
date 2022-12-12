from datetime import datetime
from typing import Optional, Sequence

from pydantic import BaseModel


class TodoListBase(BaseModel):
    name: str


# Properties to receive via API on creation
class TodoListCreate(TodoListBase):
    ...


# Properties to receive via API on update
class TodoListUpdate(TodoListBase):
    id: Optional[int] = None


class TodoListInDBBase(TodoListBase):
    id: Optional[int] = None
    user_id: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        orm_mode = True


# Additional properties stored in DB but not returned by API
class TodoListInDB(TodoListInDBBase):
    ...


# Additional properties to return via API
class TodoList(TodoListInDBBase):
    ...


class TodoListSearchResults(BaseModel):
    results: Sequence[TodoList]
