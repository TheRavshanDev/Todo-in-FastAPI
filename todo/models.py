from sqlalchemy import Column, Integer, String
from .database import Base

class Todo(Base):
    __tablename__ = 'to do list'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    text = Column(String)
    date = Column(String)
    status = Column(String)