from dataclasses import dataclass
from datetime import datetime
from unittest import TestCase
from use_cases.task.dtos.show_task import ShowTaskOutputDto


class TestCreateTaskDto(TestCase):
    @dataclass
    class ShowTaskOutputDtoMirror:
        id: int
        title: str
        description: str
        date_create: datetime
        date_update: datetime

    def test_show_task_output_types(self):
        assert self.ShowTaskOutputDtoMirror.__annotations__ == ShowTaskOutputDto.__annotations__
