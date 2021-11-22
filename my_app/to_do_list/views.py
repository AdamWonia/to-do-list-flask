from my_app import app, db
from my_app.to_do_list.models import ToDoList
from flask import request, redirect, render_template, url_for


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
        return render_template('to_do_list/index.html', tasks=tasks)


@app.route('/tasks/update/<int:id>', methods=['GET', 'POST'])
def update(id=None):
    task = ToDoList.query.get_or_404(id)
    if request.method == "POST":
        task.task_content = request.form['task_content']
        try:
            db.session.commit()
            return redirect(url_for('index'))
        except Exception as e:
            return f"Something went wrong when updating the task: {e}"
    else:
        return render_template('to_do_list/update.html', task=task)


@app.route('/tasks/delete/<int:id>')
def delete(id=None):
    task = ToDoList.query.get_or_404(id)
    try:
        db.session.delete(task)
        db.session.commit()
        return redirect(url_for('index'))
    except Exception as e:
        return f"Something went wrong when updating the task: {e}"
