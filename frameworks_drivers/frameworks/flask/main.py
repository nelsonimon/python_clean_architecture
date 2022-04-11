from typing import List, Union
from flask import Flask, abort, jsonify, request
from configuration import configuration

# import controllers
from interface_adapters.controllers.task_controller import TaskController

#import adapters
from interface_adapters.adapters.flask.task_adapter import TaskAdapter

app = Flask(__name__)
_port = configuration.settings.get("Flask","port")

############################################
@app.route("/", methods=["GET"])
def list_tasks():
    output_dto  = TaskController.list_tasks()
    output = TaskAdapter.list_task_output(output_dto)
    return output

@app.route("/create_task/", methods=["POST"])
def create_task():
    input = TaskAdapter.create_task_input(request.json)
    dto_output = TaskController.create_task(input)
    output = TaskAdapter.create_task_output(dto_output)
    return output

@app.route("/task/<id>", methods=["GET"])
def show_task(id:int):
    dto_output = TaskController.show_task(id)
    if(dto_output is None):
        return abort(404, f"id = {id}")

    output = TaskAdapter.show_task_output(dto_output)    
    return output

@app.errorhandler(404)
def resource_not_found(e):
    return jsonify(error=str(e)), 404

############################################
if __name__=="__main__":
    app.run(debug=True, port=_port)