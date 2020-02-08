from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)



@app.route("/")
def home():
	return render_template("index.html")


@app.route("/level_one")
def levOne():
	return render_template("levOne.html")


@app.route("/level_two")
def levTwo():
	return render_template("levTwo.html")


@app.route("/level_three")
def levThree():
	return render_template("levThree.html")

@app.route("/the_end")
def fin():
	return render_template("theend.html")




if __name__ == "__main__":
	app.run(debug=True)