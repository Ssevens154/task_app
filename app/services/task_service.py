from app.schemas.task_schema import Task, TaskCreate
from app.core.db import tasks, task_id_counter
from fastapi import HTTPException

def create_task(task_data: TaskCreate) -> Task:
    global task_id_counter

    task = Task(
        id=task_id_counter,
        **task_data.dict()
    )

    tasks.append(task)
    task_id_counter += 1
    return task


def get_all_tasks():
    return tasks


def get_task_by_id(task_id: int) -> Task:
    for task in tasks:
        if task.id == task_id:
            return task
    raise HTTPException(
    status_code=404,
    detail=f"Task with id {task_id} not found"
)