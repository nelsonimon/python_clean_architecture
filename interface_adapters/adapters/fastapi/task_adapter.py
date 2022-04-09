import json
from dataclasses import asdict, is_dataclass
from datetime import datetime
from typing import Any, List
import pydantic.dataclasses

#import dtos
from use_cases.task.dtos.create_task import CreateTaskInputDto, CreateTaskOutputDto
from use_cases.task.dtos.show_task import ShowTaskOutputDto

class TaskAdapterDto:
    create_task_input_dto = pydantic.dataclasses.dataclass(CreateTaskInputDto)
    create_task_output_dto = pydantic.dataclasses.dataclass(CreateTaskOutputDto)
    show_task_output_dto = pydantic.dataclasses.dataclass(ShowTaskOutputDto)

class TaskAdapter:
    
    #create task
    @classmethod
    def create_task_input(cls, request:TaskAdapterDto.create_task_input_dto)->CreateTaskInputDto:
        return CreateTaskInputDto(**asdict(request))

    @classmethod
    def create_task_output(cls, output:CreateTaskOutputDto)->TaskAdapterDto.create_task_output_dto:
        return TaskAdapterDto.create_task_output_dto(**asdict(output))
       
    #list tasks
    @classmethod
    def list_task_output(cls, output:List[ShowTaskOutputDto])->List[TaskAdapterDto.show_task_output_dto]:
        return [asdict(tasks) for tasks in output]

    #show task
    @classmethod
    def show_task_output(cls, output:ShowTaskOutputDto)->TaskAdapterDto.show_task_output_dto:
        return TaskAdapterDto.show_task_output_dto(**asdict(output))

    #private methods
    @staticmethod
    def __defaut_json_encoder(obj: object)->Any:
        if is_dataclass(obj):
            return asdict(obj)
        elif isinstance(obj, datetime):
            return obj.timestamp()
        else:
            return repr(obj)
