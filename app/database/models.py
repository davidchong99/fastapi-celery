import uuid
from typing import List, Optional
from sqlmodel import SQLModel, Field
from sqlalchemy import ARRAY, Integer, Column


class Task(SQLModel, table=True):
    task_id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    status: str
    capacity: int
    weights: List[int] = Field(sa_column=Column(ARRAY(Integer)))
    values: List[int] = Field(sa_column=Column(ARRAY(Integer)))
    solution: Optional[List[int]] = Field(
        default=None, sa_column=Column(ARRAY(Integer))
    )
