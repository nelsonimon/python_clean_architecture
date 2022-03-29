from dataclasses import dataclass
from datetime import datetime

@dataclass
class ShowTaskOutputDto:
    id: int
    title: str
    description: str
    date_create: datetime
    date_update: datetime

