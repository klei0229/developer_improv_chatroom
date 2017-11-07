from flask import Flask,render_template,request
from .forms import SignupForm
from .models import db, User


#from . import signup 

#from signup import SignupForm
from . import app

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:xyz123890xyz@localhost:5432/learningflask'


db.init_app(app)

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
		return "Success!"
	elif request.method =="GET":

		return render_template('signup.html',form = form)


if __name__ == "__main__":
	app.run(debug=True)
