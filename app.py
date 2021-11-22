from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class ToDoList(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    task_content = db.Column(db.String(200), nullable=False)
    done = db.Column(db.Boolean, default=False, nullable=False)
    created = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    def __str__(self):
        return f'Task {self.id}'


@app.route('/tasks', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        task_content = request.form['task_content']
        if task_content:
            new_task = ToDoList(task_content=task_content)
            try:
                db.session.add(new_task)
                db.session.commit()
                return redirect(url_for('index'))
            except Exception as e:
                return f"Something went wrong when adding a new task: {e}"
        else:
            return redirect(url_for('index'))
    else:
        tasks = ToDoList.query.order_by(ToDoList.created).all()
        return render_template('index.html', tasks=tasks)


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
