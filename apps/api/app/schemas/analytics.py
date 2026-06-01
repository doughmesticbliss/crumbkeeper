from pydantic import BaseModel


class AnalyticsSimulationRequest(BaseModel):
    completed_tasks: int
    delayed_tasks: int


class AnalyticsSimulationResponse(BaseModel):
    efficiency_score: float
    workload_risk: bool
    recommendation: str
