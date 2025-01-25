import logging
from uuid import uuid4, UUID
from fastapi import APIRouter, Depends, status, HTTPException
from typing import Annotated

from app.common.exceptions import TaskNotFoundException, TaskNotCompletedException
from app.components.knapsack.service import KnapsackSolverService
from app.dependencies import Dependencies
from app.components.knapsack.dto import (
    ProblemInput,
    ProblemResponse,
    SolutionResponse,
    Solution,
)

knapsack_router = APIRouter()


@knapsack_router.post(
    "/problem",
    response_model=ProblemResponse,
)
def solve_knapsack_problem(
    problem: ProblemInput,
    knapsack_solver: Annotated[
        KnapsackSolverService, Depends(Dependencies.knapsack_solver_service)
    ],
):
    result = knapsack_solver.solve(problem)

    return result


@knapsack_router.get(
    "/solution/{task_id}",
    response_model=SolutionResponse,
    status_code=200,
)
def get_knapsack_solution(
    task_id: UUID,
    knapsack_solver: Annotated[
        KnapsackSolverService, Depends(Dependencies.knapsack_solver_service)
    ],
):
    try:
        result = knapsack_solver.get_solution(task_id)
    except TaskNotFoundException:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Task id not found"
        )
    except TaskNotCompletedException:
        raise HTTPException(
            status_code=status.HTTP_202_ACCEPTED, detail="Task not completed yet"
        )

    return result
