from flask import render_template
from app import app
from api import *
from user import *

@app.route('/')
def index():
    user = {'username': 'Miguel'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/level1')
def level1():
    myUser = initializeLevelOne()
    return render_template('levOne.html', historicalData, myUser.getTotalAssets(), myUser.getStockList(), myUser.getLevel().getNumDays())

@app.route('/level2')
def level2():
    return render_template('levTwo.html')

@app.route('/level3')
def level3():
    return render_template('levThree.html')

@app.route('/end')
def endPage():
    return render_template('theend.html')
