from flask import render_template, flash
from app import app, models, db
from .createTask import CreateTask

@app.route('/')
def index():
	return render_template('todo.html',
                           title='ToDo List',
                           array=models.Todo.query.all())

@app.route('/mark_completed/<id>')
def mrk_completed(id):
	print(id)
	return ""

@app.route('/create_task', methods=['GET', 'POST'])
def create_task():
	form = CreateTask()
	if form.validate_on_submit():
		db.session.add(models.Todo(title=form.task_title.data, description=form.task_description.data, done=False))
		db.session.commit()
	return render_template('create_task.html',
							title="Create a task",
							form=form)

@app.route('/completed_tasks')
def completed_task():
	return render_template('completed_tasks.html',
							title="Completed tasks")

@app.route('/uncompleted_tasks')
def uncompleted_task():
	return render_template('uncompleted_tasks.html',
							title="Uncompleted tasks")

