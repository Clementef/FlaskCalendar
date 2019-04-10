from mongoengine import Document, StringField, ReferenceField, DateTimeField
from .User import User


class Event(Document):
    owner = ReferenceField(User)
    title = StringField()
    desc = StringField()
    date = DateTimeField(format='%Y-%m-%d')
    time = StringField()
