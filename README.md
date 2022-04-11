# python_clean_architecture
A simple to do list in python with clean architecture

![project structure](https://raw.githubusercontent.com/nelsonimon/python_clean_architecture/master/clean_architecture.png "Project Structure")

# TO RUN
1) Clone the repository
2) Create the environment folder: 
    python -m venv .venv
3) Active the environment:
    .venv\Scripts\activate
4) Install de requeriments:
    pip install -r requirements.txt
5) Choose de framework:
    In the settings.ini file, choose:
    \[Framework\]
    active: FastApi|Flask
6) Choose the data access mode:
    In the interface_adapters/controllers/task_controller.py file set the _repository:

    from frameworks_drivers.data_access.in_memory.task_repository import InMemoryTaskRepository
    _repository = InMemoryTaskRepository()

    or

    from frameworks_drivers.data_access.in_file.task_repository import InFileTaskRepository
    _repository = InFileTaskRepository()

7) To run:
    Run the main.py file in root folder
    