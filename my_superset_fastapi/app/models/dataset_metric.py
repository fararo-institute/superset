from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .base import Base


class DatasetMetric(Base):
    """Custom metrics defined for a dataset."""

    __tablename__ = "dataset_metrics"

    id = Column(Integer, primary_key=True, index=True)
    dataset_id = Column(Integer, ForeignKey("datasets.id", ondelete="CASCADE"))
    name = Column(String(255), nullable=False)
    expression = Column(String(1024), nullable=False)

    dataset = relationship("Dataset", back_populates="metrics")
