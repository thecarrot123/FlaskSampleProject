from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Length, Email

class LoginForm(FlaskForm):
    username = StringField(label='Username: ', validators=[DataRequired(), Length(min=3, max=30)])
    password = PasswordField(label='Password: ', validators=[Length(min=6)])
    login = SubmitField(label='Login')