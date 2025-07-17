from sqlalchemy import Column, DateTime, ForeignKey, func, Integer, String, Text
from sqlalchemy.orm import relationship

from .base import Base


class QueryResult(Base):
    """Store SQL execution results."""

    __tablename__ = "query_results"

    id = Column(Integer, primary_key=True, index=True)
    database_id = Column(Integer, ForeignKey("databases.id"))
    sql = Column(Text, nullable=False)
    status = Column(String(32), nullable=False, default="pending")
    started_at = Column(DateTime(timezone=True), server_default=func.now())
    finished_at = Column(DateTime(timezone=True), nullable=True)
    rows = Column(Integer, nullable=True)
    result = Column(Text, nullable=True)
    error = Column(Text, nullable=True)

    database = relationship("Database")
