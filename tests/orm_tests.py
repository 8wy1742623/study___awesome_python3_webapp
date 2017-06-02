#! python3
# -*- coding: utf-8 -*-

from orm import Model, StringField, IntegerField
import logging; logging.basicConfig(level=logging.INFO)
import asyncio
import orm


class User(Model):
    __table__ = 'test'

    id = IntegerField('id', primary_key=True)
    name = StringField('name')

# 创建实例：
user = User(id=123, name='Yud')
print(user)
user.save()
users = User.findAll()
print(users)
