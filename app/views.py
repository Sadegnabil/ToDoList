from flask import render_template, flash, redirect, url_for
from app import app, models, db
from .createTask import CreateTask
import datetime

# Create the route for the index
@app.route('/')
def index():
	return render_template('todo.html',
                           title='ToDo List',
                           array=models.Todo.query.all())


# Create the route for the completed tasks page
@app.route('/completed_tasks')
def completed_tasks():
	return render_template('completed_tasks.html',
							title="Completed tasks",
							array=models.Todo.query.all())


# Create the route for the uncompleted tasks page
@app.route('/uncompleted_tasks')
def uncompleted_tasks():
	return render_template('uncompleted_tasks.html',
							title="Uncompleted tasks",
							array=models.Todo.query.all())




# Create a route for the page used to create a new task
@app.route('/create_task', methods=['GET', 'POST'])
def create_task():
	# Create the form
	form = CreateTask()

	# Check if the form is full
	if form.validate_on_submit():
		# Add the task to the database and commit the changements
		db.session.add(models.Todo(title=form.task_title.data, description=form.task_description.data, done=False, date=datetime.datetime.utcnow()))
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
	models.Todo.query.get(id).done = not models.Todo.query.get(id).done
	db.session.commit()

	# Redirect the url to the page where the user was previously
	if page== 'completed':
		return redirect(url_for('completed_tasks'))
	elif page== 'uncompleted':
		return redirect(url_for('uncompleted_tasks'))
	else:
		return redirect(url_for('index'))


