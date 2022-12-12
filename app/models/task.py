from datetime import datetime

from sqlalchemy.sql import func
from sqlalchemy import Integer, String, Column, ForeignKey, Boolean, DateTime

from app.db.base_class import Base


class Task(Base):
    id = Column(Integer, primary_key=True, index=True)
    todo_list_id = Column(ForeignKey("todolist.id"), nullable=False)
    name = Column(String, nullable=False)
    finished = Column(Boolean, default=False)

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
