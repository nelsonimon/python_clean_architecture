from datetime import datetime
from unittest import mock, TestCase

from use_cases.task.create_task import CreateTask
from use_cases.task.dtos.create_task import CreateTaskInputDto, CreateTaskOutputDto

class TestCreateTaskUseCase(TestCase):
    
    __task_input= CreateTaskInputDto(
                    title = "Title Test 1",
                    description = "Description Test 1",
                    date_create = datetime.now(),
                    date_update = datetime.now()        
                )
    
    __create_task_success_output = CreateTaskOutputDto(
                                        success=True,
                                        error_message=""
                                )
    
    __create_task_error_output = CreateTaskOutputDto(
                                        success=False,
                                        error_message="Error"
                                )

    def test_create_task_success(self):
        with mock.patch('use_cases.task.interfaces_repositories.i_task_repository.ITaskRepository') as MockITaskRepository:
            MockITaskRepository.save.return_value = self.__create_task_success_output
            use_case = CreateTask(MockITaskRepository)
            result=use_case.execute(self.__task_input)
            assert result==self.__create_task_success_output

    def test_create_task_error(self):
        with mock.patch('use_cases.task.interfaces_repositories.i_task_repository.ITaskRepository') as MockITaskRepository:
            MockITaskRepository.save.side_effect = Exception("Error")
            use_case = CreateTask(MockITaskRepository)
            result=use_case.execute(self.__task_input)
            assert result==self.__create_task_error_output