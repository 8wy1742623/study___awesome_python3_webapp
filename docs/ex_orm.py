#! python3
# -*- coding: utf-8 -*-


# 保存数据库表的字段名 name 和字段类型 column_type
class Field(object):
    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type

    def __str__(self):
        return "<%s:%s>" % (self.__class__.__name__, self.name)


class IntegerField(Field):
    def __init__(self, name):
        super(StringField, self).__init__(name, 'bigint')


class StringField(Field):
    def __init__(self, name, column_type="varchar(100)"):
        self.name = name
        self.column_type = column_type


# todo 3 我不知道下面的内容在干什么，需要举一个例子来理解。
class ModelMetaclass(type):
    def __new__(cls, name, bases, attrs):
        if name == 'Model':
            return type.__new__(cls, name, bases, attrs)
        print("Found model: %s" % name)
        mappings = dict()
        for k, v in attrs.items():
            if isinstance(v, Field):
                print("Found mapping: %s ==> %s" % (k, v))
                mappings[k] = v
        for k in mappings.keys():
            attrs.pop(k)
        attrs['__mappings__'] = mappings
        attrs['__table__'] = name
        return type.__new__(cls, name, bases, attrs)


class Model(dict, metaclass=ModelMetaclass):
    def __init__(self, **kw):
        super(Model, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'"
                                 % key)

    def __setattr__(self, key, value):
        self[key] = value
