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
    name = CharField(unique=True, max_length=32, constraints=[SQL("COMMENT '用户名'")])
    nickname = CharField(constraints=[SQL("COMMENT '用户别名'")])
    email = CharField(constraints=[SQL("COMMENT '邮箱'")])
    password = CharField(constraints=[SQL("COMMENT '用户密码'")])
    describe = CharField(default=None, constraints=[SQL("COMMENT '描述'")])
    stated = IntegerField(default=1, constraints=[SQL("COMMENT '1：正常使用；2：禁用用户'")])
    role_id = IntegerField(default=None, constraints=[SQL("COMMENT '角色ID'")])
    create_at = DateTimeField(default=datetime.now())
    update_at = DateTimeField(null=True)

    class Meta:
        database = db
        table_name = "user"


class Role(Model):
    role_id = PrimaryKeyField()
    name = CharField(unique=True, max_length=32, constraints=[SQL("COMMENT '角色名'")])
    Permission = CharField(unique=True, constraints=[SQL("COMMENT '权限ID，字符串存储'")])
    describe = CharField(default=None)

    class Meta:
        database = db
        table_name = "role"


class Path(Model):
    path_id = PrimaryKeyField()
    path = CharField()
    describe = CharField()

    class Meta:
        database = db
        table_name = "path"


class Secrets(Model):
    secrets_id = PrimaryKeyField()
    name = CharField()
    platform = CharField()
    access_key_id = CharField(default=None)
    access_key_secret = CharField()
    zone_id = CharField(default=None)
    describe = CharField()

    class Meta:
        database = db
        table_name = "secrets"
