from flask import Flask,render_template
from forms import SignupForm

app = Flask(__name__)

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


if __name__ == "__main__":
	app.run(debug=True)
