# -*- coding: utf-8 -*-

from src.models import connect_db, close_db, db
from src.models.sys import User, Group, Route, Secrets
from src.models.refresh_cdn import RefreshHistory


db = db
connect_db()
db.create_tables([User, Group, Route, Secrets, RefreshHistory])
close_db()
