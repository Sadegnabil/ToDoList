from app import db, models

db.session.add(models.Todo(date="10/01/2017", title="First data", description="description example for the first data", done=False))
db.session.add(models.Todo(date="10/01/2016", title="Second data", description="description example for the second data", done=True))
db.session.commit()