from flask import Flask, redirect, url_for, render_template, request
from api import *
from user import *

app = Flask(__name__)

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

@app.route('/level1', methods=['GET','POST'])
def level1():
    if(request.method == 'POST'):
        if request.form['submit_button'] == 'Do Something':
            print("owo")
        elif request.form['submit_button'] == 'Do Something Else':
            print("uwu")
        else:
            print("hehe")
    else:
        myUser = initializeLevelOne()
        return render_template('levOne.html', data = myUser.getHistoricalData(), assets = myUser.getTotalAssets(), portfolio = myUser.getStockList(), numDays = myUser.getLevel().getNumDays())

@app.route('/level2')
def level2():
    return render_template('levTwo.html')

@app.route('/level3')
def level3():
    return render_template('levThree.html')

@app.route('/end')
def endPage():
    return render_template('theend.html')

if __name__ == "__main__":
    app.run(debug=True)
