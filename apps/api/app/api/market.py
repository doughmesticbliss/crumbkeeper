from fastapi import APIRouter

from app.schemas.market import MarketSimulationRequest
from app.services.market_engine import simulate_market

router = APIRouter()


@router.post("/markets/simulate")
def simulate(payload: MarketSimulationRequest):
    return simulate_market(
        payload.projected_inventory,
        payload.expected_customers,
    )
