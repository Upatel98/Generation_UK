import pymysql
import os
from dotenv import load_dotenv

load_dotenv()

connection = pymysql.connect(
    host = os.getenv("mysql_host"),
    user = os.getenv("mysql_user"),
    password = os.getenv("mysql_pass"),
    database = os.getenv("mysql_db"))