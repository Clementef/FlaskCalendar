from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
class EventForm(FlaskForm):
    title = StringField("Title")
    desc = StringField("Description")
    date = StringField("Date")
    time = StringField("time")
    submit = SubmitField("Submit")
