from flask_wtf import Form
from wtforms import TextField, TextAreaField
from wtforms.validators import DataRequired

class CreateTask(Form):
	task_title = TextField('Title', validators = [DataRequired()])
	task_description = TextAreaField('Description', validators = [DataRequired()])