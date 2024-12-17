# -*- coding: utf-8 -*-

from peewee import *
from src.models import db
from datetime import datetime

"""
CharField: 用于短文本字段（如字符串）。
TextField: 用于长文本字段。
IntegerField: 用于整数字段。
FloatField: 用于浮动字段。
DateField / DateTimeField: 用于日期和时间。
BooleanField: 用于布尔值。
"""

class User(Model):
    user_id = PrimaryKeyField()
    name = CharField(unique=True, max_length=32)
    nickname = CharField()
    email = CharField()
    password = CharField()
    title_url = CharField()
    describe = CharField(default=None)
    stated = IntegerField(default=1)
    u_group_id = IntegerField()
    create_at = DateField(datetime.now())
    update_at = DateField(null=True)

    class Meta:
        database = db
        table_name = "user"

class Group(Model):
    u_group_id = PrimaryKeyField()
    name = CharField()
    nickname = CharField()
    r_id = CharField()
    create_at = DateField(datetime.now())
    update_at = DateField(null=True)

    class Meta:
        database = db
        table_name = "group"

class Route(Model):
    r_id = PrimaryKeyField()
    path = CharField()
    describe = CharField()

    class Meta:
        database = db
        table_name = "route"

class Secrets(Model):
    secrets_id = PrimaryKeyField()
    name = CharField()
    platform = CharField()
    access_key_id = CharField()
    access_key_secret = CharField()
    describe = CharField()

    class Meta:
        database = db
        table_name = "secrets"
