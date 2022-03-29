from typing import List, Union

#import entities
from entities.task import Task

#import repository interfaces
from use_cases.task.interfaces_repositories.i_task_repository import ITaskRepository

class InMemoryTaskRepository(ITaskRepository):
    def __init__(self):
        self.tasks: List[Task] = []
        
    def get_by_id(self, id:int) -> Union[Task,None]:
        try:
            return next(task for task in self.tasks if task.id == id)
        except StopIteration:
            raise Exception

    def get_all(self) -> List[Task]:
        return self.tasks

    def save(self, task: Task) -> bool:
        try:
            if(task.id is None):
                task.id = len(self.tasks)
            self.tasks.append(task)
        except Exception:
            return False
        else:
            return True
