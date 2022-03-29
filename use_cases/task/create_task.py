#import interface repositories
from use_cases.task.interfaces_repositories.i_task_repository import ITaskRepository

#import dtos
from use_cases.task.dtos.create_task import CreateTaskInputDto, CreateTaskOutputDto

#import entities
from entities.task import Task

class CreateTask:
    def __init__(self, repository: ITaskRepository):
        self._repository = repository

    def execute(self, input_dto:CreateTaskInputDto) -> CreateTaskOutputDto:
        task = Task(
                    id = None,
                    title = input_dto.title,
                    description = input_dto.description,
                    date_create = input_dto.date_create,
                    date_update = input_dto.date_update                
                )
        
        try:
            self._repository.save(task)
        except Exception as e:
            return CreateTaskOutputDto(
                        success = False,
                        error_message = str(e)
                    )
        else:
            return CreateTaskOutputDto(
                        success = True,
                        error_message = ""
                    )
