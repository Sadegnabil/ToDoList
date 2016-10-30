from app import db, models
import sys, random

"""
Function used to generate a given number of tasks and add them to the database
Takes an argument n which is the number of tasks to generate
"""
def generate_data(n):
	for x in range(n):
		date = "%02d-%02d-%4d %02d:%02d" % (random.randint(1, 30), random.randint(1, 12), 
			random.randint(2016, 2017), random.randint(0, 23), random.randint(0, 59))
		title = "Task " + str(x)
		description = "Description example for the task " + str(x)
		state = bool(random.getrandbits(1))
		db.session.add(models.Task(date=date, title=title, description=description, done=state))
	db.session.commit()

"""
Function used to add tasks to the database with missing values
"""
def no_values_test():
	db.session.add(models.Task(title="First data", description="description example for the first data", done=False))
	db.session.add(models.Task(date="10/01/2017", description="description example for the first data", done=False))
	db.session.add(models.Task(date="10/01/2017", title="First data", done=False))
	db.session.add(models.Task(date="10/01/2017", title="First data", description="description example for the first data"))
	db.session.commit()


"""
Function used to add sample tasks to the database
"""
def sample_database():
	db.session.add(models.Task(date="27-10-2016 10:13", title="Web Application development", description="Finish the first Coursework of Web Application development", done=True))
	db.session.add(models.Task(date="27-10-2016 11:24", title="Web Application development", description="Prepare the second Coursework of Web Application development", done=False))
	db.session.add(models.Task(date="28-10-2016 15:53", title="Shopping", description="Buy cereals and milk", done=True))
	db.session.add(models.Task(date="29-10-2016 11:04", title="Software Development", description="Finish the first Coursework of Software development", done=False))
	db.session.add(models.Task(date="29-10-2016 16:15", title="Web Application labs", description="Finish the remaining lab sheets", done=False))
	db.session.add(models.Task(date="30-10-2016 09:48", title="CV", description="Finish CV and ask someone to read it", done=True))
	db.session.add(models.Task(date="30-10-2016 10:35", title="Summer Internships", description="Apply for summer internships", done=False))
	db.session.add(models.Task(date="30-10-2016 17:00", title="Operating System", description="Ask questions to J. Xu about the Operating System Coursework", done=False))
	db.session.commit()

sample_database()
