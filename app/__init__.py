from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, static_folder='static/')
app.config.from_object('config')
db = SQLAlchemy(app)
app.config['STATIC_FOLDER'] = 'static/'

from app import views, models