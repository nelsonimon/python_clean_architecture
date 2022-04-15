from datetime import datetime
from unittest import mock, TestCase

from use_cases.task.show_task import ShowTask
from use_cases.task.dtos.show_task import ShowTaskOutputDto

class TestShowTaskUseCase(TestCase):

    __show_task_success_output = ShowTaskOutputDto(
                                    id = 1,
                                    title = "Title Test 1",
                                    description = "Description Test 1",
                                    date_create = datetime.now(),
                                    date_update = datetime.now()        
                                )
    
    def test_show_task_success(self):
        _id_task:int = 1
        with mock.patch('use_cases.task.interfaces_repositories.i_task_repository.ITaskRepository') as MockITaskRepository:
            MockITaskRepository.get_by_id.return_value = self.__show_task_success_output
            use_case = ShowTask(MockITaskRepository)
            result=use_case.execute(_id_task)
            assert result==self.__show_task_success_output and result.id == _id_task

    def test_show_task_error(self):
        with mock.patch('use_cases.task.interfaces_repositories.i_task_repository.ITaskRepository') as MockITaskRepository:
            MockITaskRepository.get_by_id.side_effect = Exception("Not found")
            use_case = ShowTask(MockITaskRepository)
            result=use_case.execute(100)
            assert result==None