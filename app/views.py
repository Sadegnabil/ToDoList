from flask import render_template, flash
from app import app, models
# from .forms import CalculatorForm

@app.route('/')
def index():
    return render_template('todo.html',
                           title='Index',
                           array=models.Todo.query.all())
# @app.route('/fruit')
# def displayFruit():
#     fruits = ["Apple", "Banana", "Orange", "Kiwi"]
#     return render_template("fruit.html",fruits=fruits)

# @app.route('/loremipsum')
# def loremipsum():
# 	return render_template("loremipsum.html", title="Lorem Ipsum")

# @app.route('/calculator', methods=['GET', 'POST'])
# def calculator():
#     form = CalculatorForm()
#     if form.validate_on_submit():
#       flash('Succesfully received form data. %s + %s  = %s'%(form.num1.data, form.num2.data, form.num1.data+form.num2.data))
    
#     return render_template('calculator.html',
#                            title='Calculator',
#                            form=form)