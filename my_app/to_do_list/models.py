from my_app import db
from datetime import datetime


class ToDoList(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    task_content = db.Column(db.String(200), nullable=False)
    done = db.Column(db.Boolean, default=False, nullable=False)
    created = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    def __str__(self):
        return f'Task {self.id}'
