from pydantic import BaseModel, Field
from typing import Optional
from enum import Enum

class Status(str, Enum):
    new = "new"
    in_progress = "in_progress"
    done = "done"

class TaskCreate(BaseModel):
    title: str = Field(..., min_length=1)
    description: Optional[str] = None
    status: Status

class Task(TaskCreate):
    id: int