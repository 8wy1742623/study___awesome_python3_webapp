#!/user/bin/env python3
# -*- coding: utf-8 -*-
import sqlite3

# python 内置了轻量级的 关系型数据库 - sqlite
# 在 python 中使用 sqlite3 模块，操作数据库：
# 动作“连接数据库” -> 对象“Connection”
# “打开游标” -> 对象“Cursor”

# “Connection”对象连接到数据库文件-test.db
# 注意：如果 test.db 不存在，那么会在当前目录创建。
conn = sqlite3.connect('test.db')

# 创建游标对象“Cursor”
cursor = conn.cursor()

# 创建 user 表
cursor.execute(
    "CREATE TABLE user (id varchar(20) primary key, name varchar(20))")

# 插入一行：1，‘Yud’
cursor.execute(r"INSERT INTO user (id, name) VALUES ('1', 'Yud')")

# 查询表 - user 的行数
print(cursor.rowcount)

# 查询

# 关闭游标“Cursor”
cursor.close()

# 提交事务：
conn.commit()
# 关闭 Connection
conn.close()

# ------------------
# 1，
# insert, update, delete （增，改，删）操作
# 使用 Cursor 对象执行 insert，update，delete 语句时，
# 执行结果由 rowcount 返回影响的行数，就可以拿到执行结果。

# 2，
# select（查）操作
# 通过 fetchall() 拿到结果集（list）- 操作后表是什么样子，使用 list 表示出来。
# 结果集中，一个元素是一个 tuple，对应一行记录。

# 3，
# SQL语句中使用 python 参数，
# 那么需要把参数按照位置传递给execute()方法，有几个?占位符就必须对应几个参数，例如：
# cursor.execute(
    # 'select * from user where name=? and pwd=?', ('abc', 'password'))