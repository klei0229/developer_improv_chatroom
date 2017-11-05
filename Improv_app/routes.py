from flask import Flask,render_template,request
from signup import SignupForm
from . import app

app.secret_key = 'development-key'
@app.route("/")
def index():
	return render_template("index.html")


@app.route("/signup" , methods = ['GET','POST'])
def signup():
	form = SignupForm()
	if request.method == "POST":
		return "Success!"
	elif request.method =="GET":

		return render_template('signup.html',form = form)

@app.route("/create")
def create_page():
	return render_template("create_page.html")
