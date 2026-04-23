from fastapi import FastAPI
from app.routes.tasks import router as task_router

app = FastAPI(title="Task API")

app.include_router(task_router)