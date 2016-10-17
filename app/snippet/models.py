#!/usr/bin/python
# -*- coding: utf-8 -*-
from mongoengine import Document, StringField, ReferenceField
from user.models import User


class Snippet(Document):
    title = StringField(required=True)
    content = StringField(required=True)
    author = ReferenceField(User)
