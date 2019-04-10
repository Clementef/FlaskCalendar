from app.routes import app
from flask import render_template, session
from .Classes import User, Event

months = {'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5, 'June': 6, 'July': 7, 'August': 8, 'September': 9, 'October': 10, 'November': 11, 'December': 12}
reverseMonths = {v: k for k, v in months.items()}

@app.route('/day/<day>/<month>/<year>', methods=['GET', 'POST'])
def day(day, month, year):
    #get events and format the dates for use on the calendar
    events = Event.objects
    for event in events:
        event.date = event.date.strftime('%Y-%m-%d').split("-")
        event.date[1] = reverseMonths[int(event.date[1])]
        event.date[2] = str(int(event.date[2]))

    return render_template('day.html', day=day, month=month, year=year, events=events)
