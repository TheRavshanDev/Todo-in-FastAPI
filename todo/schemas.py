from pydantic import BaseModel


class Todo(BaseModel):
    title: str
    text: str
    date: str
    status: str

class ShowTodo(BaseModel):
    title: str
    text: str
    status: str

    class Config():
        orm_mode = True