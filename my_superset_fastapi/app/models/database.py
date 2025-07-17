from sqlalchemy import Column, DateTime, func, Integer, String
from sqlalchemy.orm import relationship

from .base import Base


class Database(Base):
    """Connection information for a database."""

    __tablename__ = "databases"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False, unique=True)
    sqlalchemy_uri = Column(String(1024), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    datasets = relationship("Dataset", back_populates="database")

    # TODO: encrypt credentials or integrate with secrets manager
