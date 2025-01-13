# -*- coding: utf-8 -*-

from src.models import connect_db, close_db, db
from src.models.sys import User, Role, Path, Secrets
from src.models.refresh_cdn import RefreshHistory


db = db
connect_db()
db.create_tables([User, Role, Path, Secrets, RefreshHistory])
close_db()
