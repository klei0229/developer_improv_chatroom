import os
from flask import Flask,render_template,request, session, redirect, url_for
from .forms import SignupForm, LoginForm
from .models import db, User
from . import app
from flask_sqlalchemy import SQLAlchemy

#postgres sql
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:xyz123890xyz@localhost:5432/learningflask'
#db.init_app(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://wfibcqxjvbzada:5ea7dff6b2fd7aa8add4fc96326defc8eadbb2a34661e1304a3de08053817567@ec2-54-235-90-125.compute-1.amazonaws.com:5432/d6s3p8sri4ie30'
db = SQLAlchemy(app)

#secretkey for login
app.secret_key = 'development-key'
@app.route("/")
def index():
    return render_template("index.html")
@app.route("/signup", methods=['GET', 'POST'])
def signup():
	form = SignupForm()
	if request.method == "POST":
		if form.validate() == False:
			return render_template('signup.html', form = form)
		else:
			newuser = User(form.first_name.data, form.last_name.data , form.email.data, form.password.data)
			db.session.add(newuser)
			db.session.commit()
			#session['email'] = newuser.email
			return redirect(url_for('index'))
	elif request.method =="GET":
		return render_template('signup.html', form = form)

#create a room decorator by jack
@app.route("/create")
def create_page():
	return render_template("create_page.html")


@app.route("/login" , methods = ["GET" , "POST"])
def login():
	form = LoginForm()
	if request.method == "POST":
		if form.validate() == False:
			return render_template("login.html" , form = form)
		else:
			email = form.email.data
			password = form.password.data
			user = User.query.filter_by(email=email).first()
			if user is not None and user.check_password(password):
				session['email'] = form.email.data
				#return redirect(url_for('home'))
				return render_template('index.html',userLoggedIn = True)
			else:
				return redirect(url_for('login'))
	elif request.method == 'GET':
		return render_template('login.html', form= form)

@app.route("/logout")
def logout():
	session.pop('email',None)
	return redirect(url_for('index'))

@app.route("/search")
def browse():
	return render_template("search.html")

@app.route("/session")
def chatroom():
	return render_template("chatroom.html")

if __name__ == "__main__":
	app.run(debug=True)
