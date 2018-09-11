from flask import Flask, redirect, render_template, url_for
app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('resume'))
	
@app.route('/resume/')
def resume():
	return render_template('resume.html')