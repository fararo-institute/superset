from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .base import Base


class DatasetColumn(Base):
    """Model for dataset columns."""

    __tablename__ = "dataset_columns"

    id = Column(Integer, primary_key=True, index=True)
    dataset_id = Column(Integer, ForeignKey("datasets.id", ondelete="CASCADE"))
    name = Column(String(255), nullable=False)
    type = Column(String(255), nullable=True)

    dataset = relationship("Dataset", back_populates="columns")
