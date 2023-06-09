from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base
from pydantic import BaseModel
from datetime import datetime

Base = declarative_base()

# SQLAlchemy model for the 'tasks' table.
class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    deadline = Column(DateTime)

# Pydantic model for representing a task.
class TaskModel(BaseModel):
    id: int
    title: str
    description: str
    deadline: datetime

    class Config:
        orm_mode = True

# Pydantic model for creating a new task.
class TaskCreate(BaseModel):
    
    title: str
    description: str
    deadline: str

# Pydantic model for updating an existing task.
class TaskUpdate(BaseModel):
    title: str
    description: str
    deadline: str



