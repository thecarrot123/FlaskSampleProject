from flask import render_template
from main import app

@app.route('/')
@app.route('/home')
@app.route('/index')
def home_page():
    return render_template("index.html")

