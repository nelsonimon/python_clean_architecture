from datetime import datetime
from dataclasses import dataclass

@dataclass
class Task:
    id: int
    title: str
    description: str
    date_create: datetime
    date_update: datetime
