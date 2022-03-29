import json
from dataclasses import asdict, is_dataclass
from datetime import datetime
from typing import Any, List

#import dtos
from use_cases.task.dtos.create_task import CreateTaskInputDto, CreateTaskOutputDto
from use_cases.task.dtos.show_task import ShowTaskOutputDto

class TaskAdapter:
    
    #create task
    @classmethod
    def create_task_input(cls, request)->CreateTaskInputDto:
        return CreateTaskInputDto(**request)

    @classmethod
    def create_task_output(cls, output:CreateTaskOutputDto)->str:
          return json.dumps(asdict(output), default=cls.__defaut_json_encoder)

    #list tasks
    @classmethod
    def list_task_output(cls, output:List[ShowTaskOutputDto])->str:
        return json.dumps(
            [asdict(tasks) for tasks in output], default=cls.__defaut_json_encoder
        )

    #private methods
    @staticmethod
    def __defaut_json_encoder(obj: object)->Any:
        if is_dataclass(obj):
            return asdict(obj)
        elif isinstance(obj, datetime):
            return obj.timestamp()
        else:
            return repr(obj)

    