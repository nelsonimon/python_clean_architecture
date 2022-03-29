from dataclasses import dataclass
from datetime import datetime

@dataclass
class CreateTaskInputDto:
    title: str
    description: str
    date_create: datetime
    date_update: datetime

@dataclass
class CreateTaskOutputDto:
    success: bool
    error_message: str

