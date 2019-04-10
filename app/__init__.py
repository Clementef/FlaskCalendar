from flask import Flask
from mongoengine import connect
import os

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY") or os.urandom(20)
connect("flaskcalendar", host='mongodb://admin:1superadmin@ds030500.mlab.com:30500/flaskcalendar')

from .routes import *
