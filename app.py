from flask import Flask, render_template
#https://www.youtube.com/watch?v=2e4STDACVA8&list=PLCC34OHNcOtqJBOLjXTd5xC0e-VD3siPn

app = Flask(__name__, static_folder='./static')

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/about')
def about():
	return render_template("about.html")

@app.route('/upcomingevents')
def upcomingevents():
	return render_template("upcomingevents.html")

@app.route('/scheduleprices')
def scheduleprices():
	return render_template("scheduleprices.html")

@app.route('/gallery')
def gallery():
	return render_template("gallery.html")

@app.route('/members')
def members():
	return  render_template("members.html")

@app.route('/information')
def information():
	return render_template("schedule+prices.html")

@app.route('/provincialteam')
def provincialteam():
	return render_template("provincialteam.html")