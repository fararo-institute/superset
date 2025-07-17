from sqlalchemy import Column, DateTime, ForeignKey, func, Integer, String, Text
from sqlalchemy.orm import relationship

from .base import Base


class Dataset(Base):
    __tablename__ = "datasets"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False, unique=True)
    database_id = Column(Integer, ForeignKey("databases.id"), nullable=True)
    schema_name = Column(String(255), nullable=True)
    table_name = Column(String(255), nullable=True)
    sql = Column(Text, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    database = relationship("Database", back_populates="datasets")
    charts = relationship("Chart", back_populates="dataset")
    columns = relationship("DatasetColumn", back_populates="dataset")
    metrics = relationship("DatasetMetric", back_populates="dataset")

    # TODO: add tags/categories relationships
