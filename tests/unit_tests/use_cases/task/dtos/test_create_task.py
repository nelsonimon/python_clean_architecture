from dataclasses import dataclass
from datetime import datetime
from unittest import TestCase
from use_cases.task.dtos.create_task import CreateTaskInputDto, CreateTaskOutputDto


class TestCreateTaskDto(TestCase):
    @dataclass
    class CreateTaskInputDtoMirror:
        title: str
        description: str
        date_create: datetime
        date_update: datetime

    @dataclass
    class CreateTaskOutputDtoMirror:
        success: bool
        error_message: str

    def test_create_task_input_types(self):
        assert self.CreateTaskInputDtoMirror.__annotations__ == CreateTaskInputDto.__annotations__
    
    def test_create_task_output_types(self):
        assert self.CreateTaskOutputDtoMirror.__annotations__ == CreateTaskOutputDto.__annotations__