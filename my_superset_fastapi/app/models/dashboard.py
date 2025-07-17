from sqlalchemy import Column, DateTime, func, Integer, String, Text
from sqlalchemy.orm import relationship

from .base import Base
from .dashboard_chart import DashboardChart


class Dashboard(Base):
    __tablename__ = "dashboards"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    layout = Column(Text, nullable=True)
    filters = Column(Text, nullable=True)
    share_token = Column(String(255), nullable=True, unique=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    charts = relationship(
        "Chart",
        secondary=DashboardChart,
        back_populates="dashboards",
    )
