#!/usr/bin/python
# -*- coding: utf-8 -*-
from mongoengine import Document, StringField, BooleanField, FileField
import settings


class User(Document):
    nickname = StringField(required=True, min=8, max=16)
    name = StringField(max=126)
    password = StringField(required=True, min=8, max=16)
    email = StringField(required=True, max=128)
    active = BooleanField(default=False)
    photo = FileField(default=settings.DEFAULT_PHOTO)
