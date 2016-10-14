from flask import render_template, flash, redirect, url_for, send_from_directory
from app import app, models, db
from .createTask import CreateTask
import datetime
import os

# Create the route for the index
@app.route('/')
def index():
	return render_template('todo.html',
                           title='ToDo List',
                           array=models.Task.query.all())


# Create the route for the completed tasks page
@app.route('/completed_tasks')
def completed_tasks():
	return render_template('completed_tasks.html',
							title="Completed tasks",
							array=models.Task.query.all())


# Create the route for the uncompleted tasks page
@app.route('/uncompleted_tasks')
def uncompleted_tasks():
	return render_template('uncompleted_tasks.html',
							title="Uncompleted tasks",
							array=models.Task.query.all())




# Create a route for the page used to create a new task
@app.route('/create_task', methods=['GET', 'POST'])
def create_task():
	# Create the form
	form = CreateTask()

	# Check if the form is full
	if form.validate_on_submit():
		# Add the task to the database and commit the changements
		db.session.add(models.Task(title=form.task_title.data, description=form.task_description.data, done=False, date=datetime.datetime.utcnow().strftime("%d-%m-%Y %H:%M")))
		db.session.commit()

		# Reset the fields
		form.task_title.data="";
		form.task_description.data="";

	return render_template('create_task.html',
							title="Create a task",
							form=form)



# Create the route used tu change the state of the task
@app.route('/toggle/<page>/<id>')
def mrk_completed(page, id):
	# Retrieve the elements using the id, change its state and commit the changements
	models.Task.query.get(id).done = not models.Task.query.get(id).done
	db.session.commit()

	# Redirect the url to the page where the user was previously
	if page== 'completed':
		return redirect(url_for('completed_tasks'))
	elif page== 'uncompleted':
		return redirect(url_for('uncompleted_tasks'))
	else:
		return redirect(url_for('index'))



# Create the route used to delete a task
@app.route('/delete/<page>/<id>')
def delete(page, id):
	# Retrieve the task using the id, delete it and commit the changements
	task = models.Task.query.get(id)
	db.session.delete(task)
	db.session.commit()

	# Redirect the url to the page where the user was previously
	if page== 'completed':
		return redirect(url_for('completed_tasks'))
	elif page== 'uncompleted':
		return redirect(url_for('uncompleted_tasks'))
	else:
		return redirect(url_for('index'))


@app.route('/favicon.png') 
def favicon(): 
	return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.png')