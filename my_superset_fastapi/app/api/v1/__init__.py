from fastapi import APIRouter

from . import charts, dashboards, databases, datasets, queries

api_router = APIRouter()
api_router.include_router(datasets.router)
api_router.include_router(charts.router)
api_router.include_router(dashboards.router)
api_router.include_router(databases.router)
api_router.include_router(queries.router)
