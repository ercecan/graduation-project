from typing import List, Optional

from beanie import Document

from .major import MajorPlan


class School(Document):
    name: str
    download_link: Optional[str] = None
    majors: Optional[List[MajorPlan]] = None

    class Settings:
        name = "schools"