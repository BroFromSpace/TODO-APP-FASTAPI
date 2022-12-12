from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session

from app import crud
from app import schemas
from  app.api import deps

router = APIRouter(
    prefix="/tasks",
    tags=["tasks"]
)


@router.post("/", status_code=201)
def create_task(
    *,
    list_id: int,
    task_name: str,
    db: Session = Depends(deps.get_db),
    current_user: schemas.User = Depends(deps.get_current_user),
):
    task = crud.task.create(db=db, list_id=list_id, task_name=task_name)

    return task


@router.patch("/{task_id}", status_code=200)
def update_task(
    task_id: int,
    task_name: str = None,
    finished: bool = None,
    *,
    db: Session = Depends(deps.get_db),
    current_user: schemas.User = Depends(deps.get_current_user)
):
    db_obj = crud.task.get(db=db, id=task_id)
    task = crud.task.update(db=db, db_obj=db_obj, obj_in={'name': task_name, 'finished': finished})

    return task


@router.delete("/{task_id}", status_code=200)
def delete_task(
    task_id: int,
    *,
    db: Session = Depends(deps.get_db),
    current_user: schemas.User = Depends(deps.get_current_user)
):
    task = crud.task.remove(db=db, id=task_id)

    return task
