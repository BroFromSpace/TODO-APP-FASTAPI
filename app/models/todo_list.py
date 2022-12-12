from sqlalchemy.sql import func
from sqlalchemy import Integer, String, Column, ForeignKey, DateTime

from app.db.base_class import Base


class TodoList(Base):
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(ForeignKey("user.id"), nullable=False)
    name = Column(String, nullable=False)

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
