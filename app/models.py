# Import db to be able to create a database model
from app import db

# Database model called Task can store a Task
class Task(db.Model):
	# 'id' is the primary key that is used to retrieve an element
	id = db.Column(db.Integer, primary_key=True)

	# 'date' is used to store a date as a String
	date = db.Column(db.String(20))

	# 'title' and 'description' stores the title and the description as Strings
	title = db.Column(db.String(50))
	description = db.Column(db.String(500))

	# 'done' stores a boolean value. If it's true the task is done. If it's false the task needs to be done
	done = db.Column(db.Boolean)