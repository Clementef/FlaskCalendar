from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField
class EventForm(FlaskForm):
    title = StringField("Title")
    desc = StringField("Description")
    date = DateField("Date", format='%Y-%m-%d')
    time = StringField("time")
    submit = SubmitField("Submit")
