from flask import render_template, redirect, url_for
from main import app, forms, db
from main.models import User

@app.route('/login', methods=["POST","GET"])
def login_page():
    loginForm = forms.LoginForm()
    if loginForm.validate_on_submit():
        return redirect(url_for('home_page'))
    return render_template('login_page.html',loginForm=loginForm)

