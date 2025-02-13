from uuid import UUID
from fastapi import APIRouter, Depends, status, HTTPException
from typing import Annotated

from app.common.exceptions import TaskNotFoundException, TaskNotCompletedException
from app.knapsack_router import service
from app.knapsack_router.dto import (
    ProblemInput,
    ProblemResponse,
    SolutionResponse,
    Solution,
)

router = APIRouter()


@router.post(
    "/problem",
    response_model=ProblemResponse,
)
def solve_knapsack_problem(problem: ProblemInput):
    result = service.solve(problem)
    return result


@router.get(
    "/solution/{task_id}",
    response_model=SolutionResponse,
    status_code=200,
)
def get_knapsack_solution(task_id: UUID):
    try:
        result = service.get_solution(task_id)
    except TaskNotFoundException:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Task id not found"
        )
    except TaskNotCompletedException:
        raise HTTPException(
            status_code=status.HTTP_202_ACCEPTED, detail="Task not completed yet"
        )

    return result
