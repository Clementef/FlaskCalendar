from app.routes import app
from flask import render_template, session, request, redirect
from .Forms import EventForm
from .Classes import Event, User
import requests


@app.route('/newevent', methods=['GET', 'POST'])
def newevent():
    form = EventForm(request.form)

    if request.method == 'POST' and form.validate():
        # get the current user for the event
        for user in User.objects:
            if user.name == session["displayName"]:
                currentUser = user

        newEvent = Event()
        newEvent.owner = currentUser
        newEvent.title = form.title.data
        newEvent.desc = form.desc.data
        newEvent.date = form.date.data
        newEvent.time = form.time.data
        newEvent.save()

        return redirect('/calendar')

    return render_template('newevent.html', form=form)
