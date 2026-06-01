from pydantic import BaseModel


class MarketSimulationRequest(BaseModel):
    projected_inventory: int
    expected_customers: int


class MarketSimulationResponse(BaseModel):
    projected_sell_through: float
    overproduction_risk: bool
    recommendation: str
