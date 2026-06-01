def simulate_analytics(
    completed_tasks: int,
    delayed_tasks: int,
):
    efficiency = completed_tasks / (
        completed_tasks + delayed_tasks
    ) if (completed_tasks + delayed_tasks) else 0

    risk = efficiency < 0.75

    recommendation = (
        "Operational strain detected."
        if risk
        else "Operational efficiency is healthy."
    )

    return {
        "efficiency_score": efficiency,
        "workload_risk": risk,
        "recommendation": recommendation,
    }
