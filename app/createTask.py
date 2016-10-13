from flask_wtf import Form
from wtforms import TextField, TextAreaField
from wtforms.validators import DataRequired
import datetime

# Create the form class used to store the submitted data before putting them in the database
class CreateTask(Form):
	task_title = TextField('Title', validators = [DataRequired()])
	task_description = TextAreaField('Description', validators = [DataRequired()])