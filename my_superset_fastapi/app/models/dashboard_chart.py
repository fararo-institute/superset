from sqlalchemy import Column, ForeignKey, Integer, Table

from .base import Base

DashboardChart = Table(
    "dashboard_charts",
    Base.metadata,
    Column("dashboard_id", Integer, ForeignKey("dashboards.id"), primary_key=True),
    Column("chart_id", Integer, ForeignKey("charts.id"), primary_key=True),
)
