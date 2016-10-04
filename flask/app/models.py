from app import db

class Todo(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	date = db.Column(db.String(11))
	title = db.Column(db.String(500))
	description = db.Column(db.String(500))
	done = db.Column(db.Boolean)