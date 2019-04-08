from app.routes import app
from flask import render_template
import calendar
cal= calendar.Calendar(6)
months = {'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5, 'June': 6, 'July': 7, 'August': 8, 'September': 9, 'October': 10, 'November': 11, 'December': 12}

def flatten(array):
  new = []
  for i in array:
    for j in i:
      new.append(j)
  return new

def getMonth(month, year):
  weeks = cal.monthdayscalendar(int(year), months[month])
  return flatten(weeks)

@app.route('/calendar', methods=['GET', 'POST'],  defaults={'month': 'April', 'year': '2019'})
@app.route('/calendar/<month>/<year>', methods=['GET', 'POST'])
def calendar(month, year):
    return render_template('calendar.html', monthName = month,
    month=getMonth(month, year), year=year, 
    weekdays=['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'])
