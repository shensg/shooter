# -*- coding: utf-8 -*-

from src.models import connect_db, close_db, db
from src.models.sys import User, Group, Route, Secrets


db = db
connect_db()
db.create_tables([User, Group, Route, Secrets])
close_db()
