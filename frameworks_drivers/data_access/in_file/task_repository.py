from dataclasses import asdict, is_dataclass
from typing import List, Union, Any
from datetime import datetime
import json
import os, os.path

#import entities
from entities.task import Task

#import repository interfaces
from use_cases.task.interfaces_repositories.i_task_repository import ITaskRepository

class InFileTaskRepository(ITaskRepository):
    def __init__(self):
        self.tasks = []
        self.dir = os.path.join(os.getcwd(),'frameworks_drivers/data_access/in_file/temp')
        
    def get_by_id(self, id:int) -> Union[Task,None]:
        self.tasks=[]
        file_path = f"{self.dir}\{id}.txt"
        if (os.path.isfile(file_path)):
            self.__read_text_file(file_path)
            return self.tasks[0]
        else:
            raise Exception("No data found")

    def get_all(self) -> List[Task]:
        self.tasks=[]
        for file in os.listdir(self.dir):
            if file.endswith(".txt"):
                file_path = f"{self.dir}\{file}"
                self.__read_text_file(file_path)

      
        return self.tasks

    def save(self, task: Task) -> bool:
        try:
            path, dirs, files = next(os.walk(self.dir))
            if(task.id is None):
                task.id = (len(files)+1) if len(files) > 0 else 1

            with open( os.path.join(self.dir,str(task.id)+'.txt'), 'w') as f:
                f.write(json.dumps(asdict(task), default=self.__defaut_json_encoder))

        except Exception:
            return False
        else:
            return True
    
    #private methods
    def __defaut_json_encoder(self, obj: object)->Any:
        if is_dataclass(obj):
            return asdict(obj)
        elif isinstance(obj, datetime):
            return obj.timestamp()
        else:
            return repr(obj)
    
    def __read_text_file(self, file_path):
        with open(file_path, 'r') as f:
            task = json.loads(f.read())
            self.tasks.append(Task(**task))

