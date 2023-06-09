from fastapi import FastAPI
from routes.task import router as task_router

app = FastAPI()

# REST API
@app.get("/")
def root():
    return {"message": "API RUNNING"}

app.include_router(task_router, prefix="/tasks", tags=["tasks"])
