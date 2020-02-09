from flask import Flask, redirect, url_for, render_template, request
from api import *
from user import *
from stock import Stock

app = Flask(__name__)

myUser = initializeLevelOne()
myUserTwo = initializeLevelTwo()

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
    return render_template('levOne.html', histData = myUser.getHistoricalData(), assets = myUser.getTotalAssets(), portfolio = myUser.getStocksBought(), currentDate = myUser.getCurrentDate())

@app.route('/level1/result/<days>', methods=['GET','POST'])
def results(days = 0):
    if (request.method == 'POST'):
        if request.form['submit_button'] == 'Do Something':
            return("owo")
        elif request.form['submit_button'] == 'Do Something Else':
            print(request.form['numBuy'])
            print(request.form['numShort'])
            for i in range(int(request.form['numBuy'])):
                myUser.buyStock(Stock('AAPL'))
            print(myUser.getStockList())
            print(request.form['buySell'])
            return("uwu")
        else:
            return("hehe")
        return render_template('index.html')
    return render_template('index.html')

@app.route('/level2', methods=['GET','POST'])
def level2():
    return render_template('levOne.html', histData = myUserTwo.getHistoricalData(), assets = myUserTwo.getTotalAssets(), portfolio = myUserTwo.getStocksBought(), currentDate = myUserTwo.getCurrentDate())

@app.route('/level2/result/<days>', methods=['GET','POST'])
def results2(days = 0):
    if (request.method == 'POST'):
        if request.form['submit_button'] == 'Do Something':
            return("owo")
        elif request.form['submit_button'] == 'Do Something Else':
            print(request.form['numBuy'])
            print(request.form['numShort'])
            for i in range(int(request.form['numBuy'])):
                myUserTwo.buyStock(Stock('AAPL'))
            print(myUserTwo.getStockList())
            print(request.form['buySell'])
            return("uwu")
        else:
            return("hehe")
        return render_template('index.html')
    return render_template('index.html')

@app.route('/level3')
def level3():
    return render_template('levThree.html')

@app.route('/end')
def endPage():
    return render_template('theend.html')

if __name__ == "__main__":
    app.run(debug=True)
