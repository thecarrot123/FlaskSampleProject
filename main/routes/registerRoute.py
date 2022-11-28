from flask import render_template, redirect, url_for
from main import app, forms, db
from main.models import User

@app.route('/register',methods=['GET','POST'])
def register_page():
    registerForm = forms.RegisterForm()
    if registerForm.register.data and registerForm.validate():
        new_user = User(
            username=registerForm.username.data,
            email=registerForm.email.data,
            password_hash=registerForm.password1.data
        )
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('data_page'))
    return render_template('register_page.html',registerForm=registerForm)