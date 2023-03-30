from typing import List
from enums.languages import Languages
from models.course import Course

class MajorPlanDto:
    name: str
    code: str
    language: Languages
    total_credits: int = 0
    courses: List[Course] = None