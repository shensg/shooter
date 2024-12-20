# -*- coding: utf-8 -*-

from peewee import *
from datetime import datetime
from src.models import db

class RefreshHistory(Model):
    id = PrimaryKeyField()
    platform = CharField(max_length=32)
    refresh_url = TextField()
    created_at = DateTimeField(default=datetime.now())

    class Meta:
        database = db
        table_name = "refresh_history"
