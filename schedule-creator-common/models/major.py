from typing import List
from pydantic import BaseModel
from enums.languages import Languages

class Major(BaseModel):
    name: str
    code: str
    language: Languages

class MajorPlan(Major):
    course_ids: List[str] = None
    total_credits: int = 0