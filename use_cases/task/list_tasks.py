from typing import List

#import interface respositories
from use_cases.task.interfaces_repositories.i_task_repository import ITaskRepository

#import dtos
from use_cases.task.dtos.show_task import ShowTaskOutputDto

#import entities
from entities.task import Task


class ListTasks:
    def __init__(self, repository: ITaskRepository):
        self._repository = repository

    def execute(self) -> List[ShowTaskOutputDto]:
        try:
            tasks:List[Task] = self._repository.get_all()
        except Exception as e:
            return []
        else:
            return [
                ShowTaskOutputDto(
                    id = task.id,
                    title = task.title,
                    description = task.description,
                    date_create = task.date_create,
                    date_update = task.date_update
                )
                for task in tasks
            ]
