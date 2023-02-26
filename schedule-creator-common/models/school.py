from typing import List, Optional

from beanie import Document

from .major import Major


class School(Document):
    name: str
    download_link: Optional[str] = None
    majors: Optional[List[Major]] = None

    class Collection:
        name = "schools"