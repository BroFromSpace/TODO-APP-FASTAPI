from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.todo_list import TodoList
from app.schemas.todo_list import TodoListCreate, TodoListUpdate, TodoListSearchResults


class CRUDTodoList(CRUDBase[TodoList, TodoListCreate, TodoListUpdate]):
    def get_all(self, db: Session, *, user_id: int) -> TodoListSearchResults:
        list_objs = db.query(TodoList).filter(TodoList.user_id == user_id).all()

        return list_objs

    def create(self, db: Session, *, user_id: int, list_name: str) -> TodoList:
        list_obj = TodoList(user_id=user_id, name=list_name)
        db.add(list_obj)
        db.commit()

        return list_obj


todo_list = CRUDTodoList(TodoList)
