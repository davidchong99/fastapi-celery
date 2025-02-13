from uuid import UUID
from typing import Self

from pydantic import (
    BaseModel,
    PositiveInt,
    model_validator,
)


class Task(BaseModel):
    task_id: UUID
    status: str
    capacity: PositiveInt
    weights: list[PositiveInt]
    values: list[PositiveInt]
    solution: list[PositiveInt] | None = None


class ProblemInput(BaseModel):
    capacity: PositiveInt
    weights: list[PositiveInt]
    values: list[PositiveInt]

    @model_validator(mode="after")
    def validate_weights_and_values_length(self) -> Self:
        if len(self.weights) != len(self.values):
            raise ValueError("Weights and values must have the same length")
        return self


class ProblemResponse(BaseModel):
    task_id: UUID
    status: str
    capacity: PositiveInt
    weights: list[PositiveInt]
    values: list[PositiveInt]


class Solution(BaseModel):
    total_value: PositiveInt
    total_weight: PositiveInt
    packed_items: list[int]


class SolutionResponse(BaseModel):
    task_id: UUID
    status: str
    capacity: PositiveInt
    weights: list[PositiveInt]
    values: list[PositiveInt]
    solution: Solution
