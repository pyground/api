import Document, StringField, BooleanField from mongoengine

class User(Document):
    nickname = StringField(required=true, min=8, max=16)
    name = StringField(max=126)
    password = StringField(required=true, min=8, max=16)
    email = StringField(required=true, max=128)
    active = BooleanField(default=false)
    photo = StringField(default=SETTINGS.DEFAULT_PHOTO)
