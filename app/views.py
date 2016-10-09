from flask import render_template, flash, redirect, url_for
from app import app, models, db
from .createTask import CreateTask

@app.route('/')
def index():
	return render_template('todo.html',
                           title='ToDo List',
                           array=models.Todo.query.all())

@app.route('/completed_tasks')
def completed_tasks():
	return render_template('completed_tasks.html',
							title="Completed tasks",
							array=models.Todo.query.all())

@app.route('/uncompleted_tasks')
def uncompleted_tasks():
	return render_template('uncompleted_tasks.html',
							title="Uncompleted tasks",
							array=models.Todo.query.all())





@app.route('/create_task', methods=['GET', 'POST'])
def create_task():
	form = CreateTask()
	if form.validate_on_submit():
		db.session.add(models.Todo(title=form.task_title.data, description=form.task_description.data, done=False))
		db.session.commit()
	return render_template('create_task.html',
							title="Create a task",
							form=form)




@app.route('/toggle/<page>/<id>')
def mrk_completed(page, id):
	models.Todo.query.get(id).done = not models.Todo.query.get(id).done
	db.session.commit()

	if page== 'completed':
		return redirect(url_for('completed_tasks'))
	elif page== 'uncompleted':
		return redirect(url_for('uncompleted_tasks'))
	else:
		return redirect(url_for('index'))


