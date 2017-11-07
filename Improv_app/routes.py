<<<<<<< HEAD
from flask import Flask,render_template,request
from .forms import SignupForm
from .models import db, User


#from . import signup 

#from signup import SignupForm
from . import app

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:xyz123890xyz@localhost:5432/learningflask'


db.init_app(app)

=======
from flask import Flask,render_template,request, sessions, redirect, url_for
from .forms import SignupForm
from .models import db, User
from . import app


#postgres sql 
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:xyz123890xyz@localhost:5432/learningflask'
db.init_app(app)

#secretkey for login
>>>>>>> 7db41aee23bbcc286bfe8e0f89141210a3b72bd8
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
<<<<<<< HEAD
		return "Success!"
=======

			#session['email'] = newuser.email
			return redirect(url_for('home'))
>>>>>>> 7db41aee23bbcc286bfe8e0f89141210a3b72bd8
	elif request.method =="GET":

		return render_template('signup.html',form = form)


<<<<<<< HEAD
if __name__ == "__main__":
	app.run(debug=True)
=======

@app.route("/home")
def home():
	return render_template('index.html')

#create a room decorator by jack
@app.route("/create")
def create_page():
	return render_template("create_page.html")

if __name__ == "__main__":
	app.run(debug=True)
	


>>>>>>> 7db41aee23bbcc286bfe8e0f89141210a3b72bd8
