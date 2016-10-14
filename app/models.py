from app import db

class Task(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	date = db.Column(db.String(20))
	title = db.Column(db.String(50))
	description = db.Column(db.String(500))
	done = db.Column(db.Boolean)