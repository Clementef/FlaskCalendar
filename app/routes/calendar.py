from app.routes import app
from flask import render_template, session
import calendar
from datetime import datetime
from .Classes import Event, User
cal= calendar.Calendar(6)

# mormal and reverse month dictionaries
months = {'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5, 'June': 6, 'July': 7, 'August': 8, 'September': 9, 'October': 10, 'November': 11, 'December': 12}
reverseMonths = {v: k for k, v in months.items()}


# Get today's month and year if there are no arguments
# Get day for calendar display
currentday = str(datetime.now().day)
currentmonth = str(datetime.now().month)
currentyear = str(datetime.now().year)


# functions to load array for month
def flatten(array):
  new = []
  for i in array:
    for j in i:
      new.append(j)
  return new

def getMonth(month, year):
  weeks = cal.monthdayscalendar(int(year), months[month])
  return flatten(weeks)


# conditional decorators (optional arguments with default values)
@app.route('/calendar', methods=['GET', 'POST'],  defaults={'month': reverseMonths[int(currentmonth)], 'year': currentyear})
@app.route('/calendar/<month>/<year>', methods=['GET', 'POST'])
def calendar(month, year):
    # Manages looping the months and going to the next Year
    nextMonthYear = year
    prevMonthYear = year
    nextMonth = (months[month]+1)
    prevMonth = (months[month]-1)
    if month == "December":
        nextMonthYear = str(int(year)+1)
        nextMonth = 1
    elif month == "January":
        prevMonthYear = str(int(year)-1)
        prevMonth = 12

    nextMonthName = reverseMonths[nextMonth]
    prevMonthName = reverseMonths[prevMonth]
    nextYear = str(int(year)+1)
    prevYear = str(int(year)-1)


    #get events and format the dates for use on the calendar
    events = Event.objects
    for event in events:
        event.date = event.date.strftime('%Y-%m-%d').split("-")
        event.date[1] = reverseMonths[int(event.date[1])]
        event.date[2] = str(int(event.date[2]))

    return render_template('calendar.html', monthName = month, nextMonthName = nextMonthName, prevMonthName = prevMonthName,
    month=getMonth(month, year), year=year, nextYear = nextYear, prevYear = prevYear, nextMonthYear = nextMonthYear, prevMonthYear = prevMonthYear,
    weekdays=['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'],
    events=events,
    currentday=currentday, currentmonth=currentmonth, monthNameReverse = months[month], currentyear=currentyear)
