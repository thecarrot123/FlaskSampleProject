from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegisterForm(FlaskForm):
    username = StringField(label='Username: ', validators=[DataRequired(), Length(min=3, max=30)])
    email = StringField(label='Email Address: ', validators=[DataRequired(), Length(max=50), Email()])
    password1 = PasswordField(label='Password: ', validators=[Length(min=6)])
    password2 = PasswordField(label='Confirm Password: ', validators=[EqualTo('password1')])
    register = SubmitField(label='Register')