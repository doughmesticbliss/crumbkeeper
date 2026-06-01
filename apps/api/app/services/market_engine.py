def simulate_market(
    projected_inventory: int,
    expected_customers: int,
):
    sell_through = (
        expected_customers / projected_inventory
        if projected_inventory else 0
    )

    overproduction = sell_through < 0.75

    recommendation = (
        "Reduce market prep volume."
        if overproduction
        else "Market prep volume is healthy."
    )

    return {
        "projected_sell_through": sell_through,
        "overproduction_risk": overproduction,
        "recommendation": recommendation,
    }
