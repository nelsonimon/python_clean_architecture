from abc import ABCMeta, abstractmethod
from typing import List, Union

from entities.task import Task

class ITaskRepository(metaclass = ABCMeta):
    @abstractmethod
    def get_by_id(self, id:int) -> Union[Task,None]:
        pass

    @abstractmethod
    def get_all(self) -> List[Task]:
        pass

    @abstractmethod
    def save(self, task: Task) -> bool:
        pass
