from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Length

class DataSubmitForm(FlaskForm):
    data = StringField(label='Add data', validators=[Length(min=1)])
    submit = SubmitField(label='Submit')

class DataClearForm(FlaskForm):
    clear = SubmitField(label='Clear Table')