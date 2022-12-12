from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.task import Task
from app.schemas.task import TaskCreate, TaskUpdate, TaskSearchResults


class CRUDTask(CRUDBase[Task, TaskCreate, TaskUpdate]):
    def get_all(self, db: Session, *, list_id: int) -> TaskSearchResults:
        task_objs = db.query(Task).filter(Task.todo_list_id == list_id).all()

        return task_objs

    def create(self, db: Session, *, list_id: int, task_name: str) -> Task:
        task_obj = Task(todo_list_id=list_id, name=task_name)
        db.add(task_obj)
        db.commit()

        return task_obj


task = CRUDTask(Task)
