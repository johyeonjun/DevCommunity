# -*- coding: utf-8 -*-
import os

SERVER_AUTO = True

if SERVER_AUTO:
    SERVER_TYPE = os.environ.get('S_TYPE')

if SERVER_TYPE == None or SERVER_AUTO == False:
    SERVER_TYPE = "LOCAL"  ## AUTO, LOCAL,  STAGING,  REAL,  UNITTEST

if SERVER_TYPE == "LOCAL" :
    DB_NAME = "DevCommunity_Test"
    # DB_NAME = "aw_aderp_test"
    DB_USER = "root"
    DB_PASSWORD = "1234"
    # DB_HOST = "127.0.0.1"
    DB_HOST = "127.0.0.1"
    DB_PORT = 3306
#     DB_NAME = "dev_qna"
#     #DB_NAME = "aw_aderp_test"
#     DB_USER = "mm_user"z
#     DB_PASSWORD = "m2_17_sql"
#     #DB_HOST = "127.0.0.1"
#     DB_HOST = "localhost"
#     DB_PORT = 3306

elif SERVER_TYPE == "REAL" :
    DB_NAME = "DevCommunity"
    DB_USER = ""
    DB_PASSWORD = ""
    DB_HOST = ""
    DB_PORT = 3306



