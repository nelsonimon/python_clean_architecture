from datetime import datetime
from unittest import mock, TestCase

from use_cases.task.list_tasks import ListTasks
from use_cases.task.dtos.show_task import ShowTaskOutputDto

class TestListTasksUseCase(TestCase):
    
    __tasks=[ShowTaskOutputDto(
                    id = 1,
                    title = "Title Test 1",
                    description = "Description Test 1",
                    date_create = datetime.now(),
                    date_update = datetime.now()        
                ), ShowTaskOutputDto(
                    id = 2,
                    title = "Title Test 2",
                    description = "Description Test 2",
                    date_create = datetime.now(),
                    date_update = datetime.now()        
                )
            ]
    def test_list_tasks(self):
        with mock.patch('use_cases.task.interfaces_repositories.i_task_repository.ITaskRepository') as MockITaskRepository:
            MockITaskRepository.get_all.return_value = self.__tasks
            use_case = ListTasks(MockITaskRepository)
            result=use_case.execute()
            assert result==self.__tasks