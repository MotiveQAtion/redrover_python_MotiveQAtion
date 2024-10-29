from pydantic import BaseModel
from enum import Enum


class Priority(str, Enum):
    low = "низкий"
    medium = "средний"
    high = "высокий"


class Case(BaseModel):
    id: int
    name: str
    description: str
    priority: Priority
    steps: list[str]
    expected_result: str
