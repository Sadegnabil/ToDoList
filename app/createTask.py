# Import the datetime to be able to retrieve the time and Form with wtforms classes to be able to create the form and validate the data
from flask_wtf import Form
from wtforms import TextField, TextAreaField
from wtforms.validators import DataRequired
import datetime

# Create the form class used to store the submitted data before putting them in the database
class CreateTask(Form):
	# Title of the task
	task_title = TextField('Title', validators = [DataRequired()])

	# Description of the task
	task_description = TextAreaField('Description', validators = [DataRequired()])