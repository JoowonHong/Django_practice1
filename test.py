import sqlite3
import datetime

now= datetime.datetime.now()

nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')
print('nowDatetime : ',nowDatetime)
print("now: ", now)

print('sqlite3.version : ', sqlite3.version)
print('sqlite3.sqite_version : ',sqlite3.sqlite_version)

#DB 생성 & Auto commit

