# db_config.py

from peewee import *
import pymysql
from config import db_config

# 安装 PyMySQL 作为 MySQL 驱动
pymysql.install_as_MySQLdb()


# 初始化 MySQL 数据库连接
db = MySQLDatabase(
    db_config["database"],
    user=db_config["user"],
    password=db_config["password"],
    host=db_config["host"],
    port=db_config["port"],
    charset=db_config["charset"]
)

def connect_db():
    """连接数据库"""
    try:
        db.connect()
        print("Database connected successfully!")
    except OperationalError as e:
        print(f"Error connecting to database: {e}")
        raise

def close_db():
    """关闭数据库连接"""
    db.close()
