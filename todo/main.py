from fastapi import FastAPI, Depends, status
from sqlalchemy.orm import Session
from .database import SessionLocal, engine
from . import models, schemas
from .models import Todo

models.Base.metadata.create_all(engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app = FastAPI()

@app.get("/tasks/", status_code=status.HTTP_200_OK)
async def task(db:Session=Depends(get_db)):
    tasks = db.query(Todo).all()
    return tasks

@app.post("/tasks/new/", status_code=status.HTTP_201_CREATED)
async def new_task(request: schemas.Todo,db:Session=Depends(get_db)):
    task = models.Todo(title=request.title, text=request.text, date=request.date, status=request.status)
    db.add(task)
    db.commit()
    db.refresh(task)
    return f'Successfully added! {task.title}'
