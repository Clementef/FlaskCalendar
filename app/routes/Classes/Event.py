from mongoengine import Document, StringField, ReferenceField
from .User import User


class Event(Document):
    owner = ReferenceField(User)
    title = StringField()
    desc = StringField()
    date = StringField()
    time = StringField()
