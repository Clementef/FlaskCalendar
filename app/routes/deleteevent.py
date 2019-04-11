import requests
from app.routes import app
from flask import render_template, session, redirect, request
from .Classes import User,Event

@app.route('/deleteevent/<id>', methods=['GET', 'POST'])
def deleteevent(id):
    for event in Event.objects:
        if str(event.id) == id:
            print('found')
            event.delete()
            return redirect('/calendar')
    return render_template("index.html")
