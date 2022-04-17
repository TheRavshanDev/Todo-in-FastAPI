from pydantic import BaseModel


class Todo(BaseModel):
    title: str
    text: str
    date: str
    status: str