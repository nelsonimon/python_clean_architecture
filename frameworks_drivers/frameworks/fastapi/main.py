from typing import Dict, List, Optional
import uvicorn
from fastapi import Body, FastAPI, HTTPException
from fastapi.encoders import jsonable_encoder
from configuration import configuration

# import controllers
from interface_adapters.controllers.task_controller import TaskController

# import adapters
from interface_adapters.adapters.fastapi.task_adapter import TaskAdapter, TaskAdapterDto

app = FastAPI()
_port = configuration.settings.get("FastApi","port")

############################################
@app.get("/", response_model=List[TaskAdapterDto.show_task_output_dto])
def list_tasks() -> List[TaskAdapterDto.show_task_output_dto]:
    dto_output = TaskController.list_tasks()
    output = TaskAdapter.list_task_output(dto_output)
    return jsonable_encoder(output)

@app.post("/create_task", response_model=TaskAdapterDto.create_task_output_dto)
def create_task(request:TaskAdapterDto.create_task_input_dto) -> TaskAdapterDto.create_task_output_dto:
    input = TaskAdapter.create_task_input(request)
    dto_output = TaskController.create_task(input)
    output = TaskAdapter.create_task_output(dto_output)
    return jsonable_encoder(output)

@app.get("/task/{id}", response_model=TaskAdapterDto.show_task_output_dto)
def show_task(id:int) -> TaskAdapterDto.show_task_output_dto:
    dto_output = TaskController.show_task(id)
    if(dto_output is None):
        raise HTTPException(status_code=404, detail=f"id = {id}")

    output = TaskAdapter.show_task_output(dto_output)
    return jsonable_encoder(output)

############################################
if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=int(_port), log_level="info", reload=True)