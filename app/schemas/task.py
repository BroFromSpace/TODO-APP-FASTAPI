from datetime import datetime
from typing import Optional, Sequence

from pydantic import BaseModel


class TaskBase(BaseModel):
    name: str


# Properties to receive via API on creation
class TaskCreate(TaskBase):
    todo_list_id: Optional[int] = None


# Properties to receive via API on update
class TaskUpdate(TaskBase):
    id: Optional[int] = None
    finished: Optional[bool] = False


class TaskInDBBase(TaskBase):
    id: Optional[int] = None
    todo_list_id: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        orm_mode = True


# Additional properties stored in DB but not returned by API
class TaskInDB(TaskInDBBase):
    ...


# Additional properties to return via API
class Task(TaskInDBBase):
    ...


class TaskSearchResults(BaseModel):
    results: Sequence[Task]
