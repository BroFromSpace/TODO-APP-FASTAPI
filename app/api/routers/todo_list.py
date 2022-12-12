from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session

from app import crud
from app import schemas
from app.api import deps

router = APIRouter(
    prefix="/todo-lists",
    tags=["todo-lists"]
)


@router.get("/{list_id}", status_code=200)
def purchase_by_id(
    list_id: int,
    *,
    db: Session = Depends(deps.get_db),
    current_user: schemas.User = Depends(deps.get_current_user)
):
    todo_list = crud.todo_list.get(db=db, id=list_id)
    tasks = crud.task.get_all(db=db, list_id=list_id)

    return {"todo list": todo_list, "tasks": tasks}


@router.get("/", status_code=200)
def purchase_all(
    *,
    db: Session = Depends(deps.get_db),
    current_user: schemas.User = Depends(deps.get_current_user)
):
    todo_lists = crud.todo_list.get_all(db=db, user_id=current_user.id)

    return {"results": todo_lists}


@router.post("/", status_code=201)
def create_list(
    *,
    list_name: str,
    db: Session = Depends(deps.get_db),
    current_user: schemas.User = Depends(deps.get_current_user),
):
    todo_list = crud.todo_list.create(db=db, user_id=current_user.id, list_name=list_name)

    return todo_list


@router.patch("/{list_id}", status_code=200)
def update_list(
    list_id: int,
    list_name: str,
    *,
    db: Session = Depends(deps.get_db),
    current_user: schemas.User = Depends(deps.get_current_user)
):
    db_obj = crud.todo_list.get(db=db, id=list_id)
    todo_list = crud.todo_list.update(db=db, db_obj=db_obj, obj_in={'name': list_name})

    return todo_list


@router.delete("/{list_id}", status_code=200)
def delete_list(
    list_id: int,
    *,
    db: Session = Depends(deps.get_db),
    current_user: schemas.User = Depends(deps.get_current_user)
):
    todo_list = crud.todo_list.remove(db=db, id=list_id)

    return todo_list
