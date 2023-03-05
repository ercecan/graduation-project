from pydantic import BaseModel
from typing import Optional

class Classroom(BaseModel):
    building: Optional[str] = None
    room: Optional[str] = None