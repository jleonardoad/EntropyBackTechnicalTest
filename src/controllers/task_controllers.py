from fastapi import HTTPException
from typing import List
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from models.task_models import Task ,TaskCreate
from services.database import get_db_session


# Retrieves a list of tasks from the database.
def get_tasks() -> List[Task]:
   
    try:
        db: Session = get_db_session()
        tasks: List[Task] = db.query(Task).all()
        return tasks
    except SQLAlchemyError:
        raise HTTPException(status_code=400, detail="Error al obtener las tareas")
        

# Retrieves a task by its ID from the database.
def get_task(task_id: int) -> Task:
    try:
        db: Session = get_db_session()
        task: Task = db.query(Task).filter(Task.id == task_id).first()
        if not task:
            raise HTTPException(status_code=404, detail="Task not found")
        return task
    except SQLAlchemyError:
        raise HTTPException(status_code=400, detail="Error al obtener las tareas")
        

# Creates a new task in the database.
def create_task(task: TaskCreate):
    try:
        with get_db_session() as db:
            db_task = Task(title=task.title, description=task.description, deadline=task.deadline)
            db.add(db_task)
            db.commit()
            db.refresh(db_task)
            return {
                "id": db_task.id,
                "title": db_task.title,
                "description": db_task.description,
                "deadline": task.deadline
            }
    except SQLAlchemyError:
        raise HTTPException(status_code=400, detail="Error al crear la tarea")


# Updates an existing task with the provided task_id in the database.
def update_task(task_id: int, updated_task: Task) -> Task:
    try:
        db: Session = get_db_session()
        task: Task = db.query(Task).filter(Task.id == task_id).first()
        if not task:
            raise HTTPException(status_code=404, detail="Task not found")
        task.title = updated_task.title
        task.description = updated_task.description
        task.deadline = updated_task.deadline
        db.commit()
        db.refresh(task)
        return task
    except SQLAlchemyError:
        raise HTTPException(status_code=400, detail="Error al actualizar task")
        

# Deletes an existing task with the provided task_id from the database
def delete_task(task_id: int):
    try:
        db: Session = get_db_session()
        task: Task = db.query(Task).filter(Task.id == task_id).first()
        if not task:
            raise HTTPException(status_code=404, detail="Task not found")
        db.delete(task)
        db.commit()
    except SQLAlchemyError:
        raise HTTPException(status_code=400, detail="Error eliminar task")
