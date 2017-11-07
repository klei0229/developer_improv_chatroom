from flask import Flask,render_template,request
from .forms import SignupForm
#from . import signup 
#from signup import SignupForm
from . import app


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
			
		return "Success!"
	elif request.method =="GET":

		return render_template('signup.html',form = form)


if __name__ == "__main__":
	app.run(debug=True)
