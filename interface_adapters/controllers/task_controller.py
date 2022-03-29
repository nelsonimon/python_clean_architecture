
from typing import List

#import use cases
from use_cases.task.create_task import CreateTask
from use_cases.task.list_tasks import ListTasks

#import dtos
from use_cases.task.dtos.create_task import CreateTaskInputDto, CreateTaskOutputDto
from use_cases.task.dtos.show_task import ShowTaskOutputDto

#import repository
#from frameworks_drivers.data_access.in_memory.task_repository import InMemoryTaskRepository
from frameworks_drivers.data_access.in_file.task_repository import InFileTaskRepository
class TaskController:

    _repository = InFileTaskRepository()

    @classmethod
    def list_tasks(cls)->List[ShowTaskOutputDto]:
        use_case = ListTasks(cls._repository)
        output:List[ShowTaskOutputDto,None] = use_case.execute()
        return output

    @classmethod
    def create_task(cls,input:CreateTaskInputDto) -> CreateTaskOutputDto:
        use_case = CreateTask(cls._repository)
        output:CreateTaskOutputDto = use_case.execute(input)
        return output