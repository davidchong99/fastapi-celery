import logging
from uuid import UUID


from app.common.exceptions import TaskNotCompletedException
from app.components.knapsack.dto import (
    ProblemResponse,
    ProblemInput,
    SolutionResponse,
    Solution,
)
from app.components.knapsack.celery_tasks import solve_knapsack_task


class KnapsackSolverService:
    def __init__(self):
        pass

    def solve(self, problem: ProblemInput):
        result = solve_knapsack_task.apply_async(
            kwargs={"status": "PENDING", **problem.model_dump()}
        )

        return ProblemResponse(
            task_id=result.id,
            status="PENDING",
            capacity=problem.capacity,
            weights=problem.weights,
            values=problem.values,
        )

    def get_solution(self, task_id: UUID):
        # Try to retrieve solution from celery backend
        result = solve_knapsack_task.AsyncResult(str(task_id))
        print(f"service result.ready(): {result.ready()}")
        print(f"service result.successful(): {result.successful()}")
        print(f"service result.failed: {result.failed()}")
        if not result.ready():
            raise TaskNotCompletedException

        data = result.get()
        print(f"service data: {data}")

        return SolutionResponse(
            task_id=task_id,
            status=data["status"],
            capacity=data["capacity"],
            weights=data["weights"],
            values=data["values"],
            solution=Solution(
                total_value=data["total_value"],
                total_weight=data["total_weight"],
                packed_items=data["packed_items"],
            ),
        )
