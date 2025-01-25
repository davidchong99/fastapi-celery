import logging

from celery.result import AsyncResult, allow_join_result
from ortools.algorithms.python import knapsack_solver
from app.create_celery_app import celery_app


@celery_app.task()
def solve_knapsack_task(**kwargs):
    capacities = [kwargs["capacity"]]
    weights = [kwargs["weights"]]
    values = kwargs["values"]

    solver = knapsack_solver.KnapsackSolver(
        knapsack_solver.SolverType.KNAPSACK_MULTIDIMENSION_BRANCH_AND_BOUND_SOLVER,
        "KnapsackExample",
    )

    solver.init(values, weights, capacities)
    computed_value = solver.solve()
    packed_items = []
    packed_weights = []
    total_weight = 0
    print("Total value =", computed_value)
    for i in range(len(values)):
        if solver.best_solution_contains(i):
            packed_items.append(i)
            packed_weights.append(weights[0][i])
            total_weight += weights[0][i]
    print("Total weight:", total_weight)
    print("Packed items:", packed_items)
    print("Packed_weights:", packed_weights)

    # Saved in celery backend
    return {
        "status": "COMPLETED",
        "values": kwargs["values"],
        "weights": kwargs["weights"],
        "capacity": kwargs["capacity"],
        "total_value": computed_value,
        "total_weight": total_weight,
        "packed_items": packed_items,
    }
