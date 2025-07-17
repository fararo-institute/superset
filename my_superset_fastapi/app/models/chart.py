from enum import Enum as PyEnum

from sqlalchemy import Column, DateTime, Enum, ForeignKey, func, Integer, String, Text
from sqlalchemy.orm import relationship

from .base import Base
from .dashboard_chart import DashboardChart


class Chart(Base):
    __tablename__ = "charts"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    dataset_id = Column(Integer, ForeignKey("datasets.id"), nullable=False)

    class ChartType(PyEnum):
        PIE = "pie"
        BAR = "bar"
        TIME_SERIES = "time_series"
        TABLE = "table"

    chart_type = Column(Enum(ChartType), nullable=False, default=ChartType.TABLE)
    config = Column(Text, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    dataset = relationship("Dataset", back_populates="charts")
    dashboards = relationship(
        "Dashboard",
        secondary=DashboardChart,
        back_populates="charts",
    )
