from app import db, models

db.session.add(models.Task(date="10/01/2017", title="First data", description="description example for the first data", done=False))
db.session.add(models.Task(date="10/01/2016", title="Second data", description="description example for the second data", done=True))
db.session.add(models.Task(date="10/01/2017", title=" 3 data", description="description example for the 3 data", done=False))
db.session.add(models.Task(date="10/01/2017", title=" 4 data", description="description example for the 4 data", done=True))
db.session.add(models.Task(date="10/01/2017", title=" 5 data", description="description example for the 5 data", done=False))
db.session.add(models.Task(date="10/01/2017", title=" 6 data", description="description example for the 6 data", done=False))
db.session.add(models.Task(date="10/01/2017", title=" 7 data", description="description example for the 7 data", done=True))
db.session.add(models.Task(date="10/01/2017", title=" 8 data", description="description example for the 8 data", done=False))
db.session.add(models.Task(date="10/01/2017", title=" 9 data", description="description example for the 9 data", done=False))
db.session.add(models.Task(date="10/01/2017", title=" 10 data", description="description example for the 10  data", done=True))
db.session.add(models.Task(date="10/01/2017", title=" 11 data", description="description example for the 11 data", done=False))
db.session.commit()