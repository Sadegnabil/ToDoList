from app import db, models
import sys, random


def test(n):
	for x in range(n):
		date = "%02d-%02d-%4d %02d:%02d" % (random.randint(1, 30), random.randint(1, 12), 
			random.randint(2016, 2017), random.randint(0, 23), random.randint(0, 59))
		title = "Task " + str(x)
		description = "Description example for the task " + str(x)
		state = bool(random.getrandbits(1))
		db.session.add(models.Task(date=date, title=title, description=description, done=state))
	db.session.commit()

test(int(sys.argv[1]))

