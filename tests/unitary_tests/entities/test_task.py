import uuid
from datetime import datetime

#import modules tests
from entities.task import Task

def test_task_entity_unit():
    id = uuid.uuid4()
    date_now = datetime.now()
    title = "Title Test"
    description = "Description Test"
    task = Task(
            id = id,
            title = title,
            description = description,
            date_create = date_now,
            date_update = date_now        
        )

    assert task.id == id
    assert task.title == title
    assert task.description == description
    assert task.date_create == date_now
    assert task.date_update == date_now