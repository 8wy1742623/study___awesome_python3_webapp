#! python3
# -*- coding: utf-8 -*-

import pymysql

# 打开数据库连接
db = pymysql.connect('localhost', 'root', 'your_password64', 'study_python_01')

# 使用 cursor() 方法建立一个游标对象 cursor
cursor = db.cursor()

# # 1，
# # 使用 execute() 方法执行 SQL 查询
# cursor.execute("SELECT VERSION()")
# # 使用 fetchone() 方法获取单条数据
# data = cursor.fetchone()
# print("Database version : %s" % data)

# 2，
# Python查询Mysql使用 fetchone() 方法获取单条数据, 使用fetchall() 方法获取多条数据。
# fetchone(): 该方法获取下一个查询结果集。结果集是一个对象
# fetchall(): 接收全部的返回结果行.
# rowcount: 这是一个只读属性，并返回执行execute()方法后影响的行数。


db.close()
