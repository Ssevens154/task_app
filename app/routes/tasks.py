from fastapi import APIRouter
from typing import List
from app.schemas.task_schema import Task, TaskCreate
from app.services.task_service import (
    create_task,
    get_all_tasks,
    get_task_by_id
)

router = APIRouter(prefix="/tasks", tags=["Tasks"])


@router.post("/", response_model=Task)
def create(task: TaskCreate):
    return create_task(task)


@router.get("/", response_model=List[Task])
def get_all():
    return get_all_tasks()


@router.get("/{task_id}", response_model=Task)
def get_one(task_id: int):
    return get_task_by_id(task_id)