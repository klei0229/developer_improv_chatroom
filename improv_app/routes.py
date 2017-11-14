from flask import Flask,render_template,request, sessions, redirect, url_for
from .forms import SignupForm
from .models import db, User
from . import app



#postgres sql
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:xyz123890xyz@localhost:5432/learningflask'
db.init_app(app)

#secretkey for login

app.secret_key = 'development-key'

@app.route("/")
def index():
	return render_template("index.html")


@app.route("/signup" , methods = ['GET','POST'])
def signup():
	form = SignupForm()
	if request.method == "POST":
		if form.validate() == False:
			return render_template('signup.html',form = form)
		else:
			newuser = User(form.first_name.data, form.last_name.data , form.email.data, form.password.data)

			db.session.add(newuser)
			db.session.commit()

			#session['email'] = newuser.email
			return redirect(url_for('home'))
	elif request.method =="GET":

		return render_template('signup.html',form = form)

#create a room decorator by jack
@app.route("/create")
def create_page():
	return render_template("create_page.html")

@app.route("/search")
def browse_comedy():
	return render_template("search.html")


if __name__ == "__main__":
	app.run(debug=True)
