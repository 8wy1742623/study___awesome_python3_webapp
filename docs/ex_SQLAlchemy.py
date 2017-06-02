#! python3
# -*- coding: utf-8 -*-

# 把关系数据库的表结果映射到对象上：
# 数据库表是一个二维表。
# 如：
# [
#     ('1', 'Michael'),
#     ('2', 'Bob'),
#     ('3', 'Adam')
# ]

# 如果把一个 tuple 用 class 实例表示出来，那么更加容易看出表的结构。
# class User(object):
#     def __init__(self, id, name):
#         self.id = id
#         self.name = name

# [
#     User('1', 'Micheal'),
#     User('2', 'Bob'),
#     User('3', 'Adam')
# ]

# 实现这样的技术称为：ORM - Object Relational Mapping。

# 注意，使用 py xx.py 格式，用 python3 解释器来运行这个脚本。
# 因为 python2 没有模块 sqlalchemy。
# 因为 python 在系统变量中默认为 python 2的解释器。
# 而 py 命令，可以使用 python 3 的 启动器-py.exe。
# 该启动器会根据文件的参数，指定使用 python 2 还是 python 3。
# 1，py -3 xx.py 会使用 python 3
# 2，py xx.py，这时会读取 .py 文件头部的信息，
# #! python3 或者是这样 #! python2 
# 会使用对应的解释器


from sqlalchemy import Column, String, Integer, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 对象的基类
Base = declarative_base()


# 定义 User 对象/类
class User(Base):
    # 表名
    __tablename__ = 'employee'

    # 表的结构
    # 注意：下面 id，name 变量的命名有一个要求：
    # 必须是与数据库的列名(field)是相同的字符串，否则在查询的时候，找不到。
    # todo 1 但是，如果需要添加列名呢？？

    # 注意 1：这里 Column 中参数 String(20)，可以对应
    # 数据库中的 varchar(20) 类型
    # Integer 对应数据库中的 int
    # 注意 2：这里 id，first_name 等属性是类的属性，而不是实例属性。
    id = Column(String(20), primary_key=True)
    first_name = Column(String(20))
    age = Column(Integer())
    sex = Column(String(12))
    income = Column(Integer())

# 初始化数据库连接 
# 连接信息的格式：
# '数据库类型+数据库驱动名称://用户名:口令@机器地址:端口号/数据库名'
engine = create_engine(\
    "mysql+pymysql://root:your_password64@localhost:3306/study_python_01")
# 创建 DBSession 对象
DBSession = sessionmaker(bind=engine)

# # 已经增加了这一行数据，后面运行的时候，再次执行，会导致，重复插入，
# # 由于，主键不能够重复，即 id 不能重复，因此再次运行增加一行数据的操作会出错。
# # 增加一行：id 3， first_name ‘Bob’。
# # 创建 session 对象
# session = DBSession()
# # 新的 User 对象
# new_user = User(id='3', first_name='Bob')
# session.add(new_user)
# session.commit()
# session.close()

# 查询数据
session = DBSession()
# 创建 Query 查询，filter 是 WHERE 条件，然后调用 one() 返回唯一行，
# 如果调用 all()，则返回所有行
user = session.query(User).filter(User.id == '3').one()

# 打印对象的类型和他的 name 属性
print('type :', type(user)) # <class '__mian__.User'>
print('name :', user.first_name) # 'Bob'
session.close()


# 预测结果
# 
