from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class DataSubmitForm(FlaskForm):
    data = StringField(label='Add data')
    submit = SubmitField(label='Submit')

class DataClearForm(FlaskForm):
    clear = SubmitField(label='Clear Table')