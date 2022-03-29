from typing import Dict, List, Optional
import uvicorn

from fastapi import Body, FastAPI
from fastapi.encoders import jsonable_encoder
#from pydantic import BaseModel

from configuration import configuration

# import controllers
from interface_adapters.controllers.task_controller import TaskController

# import adapters
from interface_adapters.adapters.fastapi.task_adapter import TaskAdapter, TaskAdapterDto

app = FastAPI()
_port = configuration.settings.get("FastApi","port")

############################################
@app.get("/", response_model=List[TaskAdapterDto.list_task_output_dto])
def listar_tarefas() -> List[TaskAdapterDto.list_task_output_dto]:
    dto_output = TaskController.list_tasks()
    output = TaskAdapter.list_task_output(dto_output)
    return jsonable_encoder(output)

@app.post("/criar_tarefa", response_model=TaskAdapterDto.create_task_output_dto)
def criar_tarefa(request:TaskAdapterDto.create_task_input_dto) -> TaskAdapterDto.create_task_output_dto:
    input = TaskAdapter.create_task_input(request)
    dto_output = TaskController.create_task(input)
    output = TaskAdapter.create_task_output(dto_output)
    return jsonable_encoder(output)

############################################
if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=int(_port), log_level="info", reload=True)