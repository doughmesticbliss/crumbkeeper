from fastapi import APIRouter

from app.schemas.analytics import AnalyticsSimulationRequest
from app.services.analytics_engine import simulate_analytics

router = APIRouter()


@router.post("/analytics/simulate")
def simulate(payload: AnalyticsSimulationRequest):
    return simulate_analytics(
        payload.completed_tasks,
        payload.delayed_tasks,
    )
