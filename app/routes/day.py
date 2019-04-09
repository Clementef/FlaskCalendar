from app.routes import app
from flask import render_template


@app.route('/day/<day>/<month>/<year>', methods=['GET', 'POST'])
def day(day, month, year):
    return render_template('day.html', day=day, month=month, year=year)
