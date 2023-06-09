from fastapi import APIRouter
from typing import List
from controllers.task_controllers import get_tasks, get_task, create_task, update_task, delete_task
from models.task_models import Task, TaskCreate, TaskUpdate, TaskModel

router = APIRouter()

# Endpoint to retrieve all tasks. Returns: List of tasks.
@router.get("/", response_model=List[TaskModel])
def read_tasks():
    tasks: List[Task] = get_tasks()
    return tasks

# Endpoint to retrieve a specific task. task_id: ID of the task to retrieve
@router.get("/{task_id}", response_model=TaskModel)
def read_task(task_id: int):
    task: Task = get_task(task_id)
    return task

# Endpoint to create a new task. Returns: The created task.
@router.post("/", response_model=TaskModel)
def create_new_task(task: TaskCreate):
    created_task: Task = create_task(task)
    return created_task

# Endpoint to update an existing task. task_id: ID of the task to update.
@router.put("/{task_id}", response_model=TaskModel)
def update_existing_task(task_id: int, task: TaskUpdate):
    updated_task: Task = update_task(task_id, task)
    return updated_task


# Endpoint to delete an existing task. task_id: ID of the task to delete
@router.delete("/{task_id}")
def delete_existing_task(task_id: int):
    delete_task(task_id)
    return {"message": "Task deleted successfully"}
