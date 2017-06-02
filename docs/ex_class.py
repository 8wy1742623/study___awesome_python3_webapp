# -*- coding: utf-8 -*-

# 1
# __getattr__ 练习的复习

# 位置：教程，面向对象高级编程 - 定制类


# python 机制介绍：
# 调用类不存在的属性时，
# 使用 __getattr__ 方法，能够让使用者调用不存在的属性。
# 或者说，使类具有动态的，由使用者决定的属性/方法。

# # 例子一：
#
#
# class Student(object):
#
#     def __init__(self):
#         self.name = "Yud"
#
#     # 给当前类动态添加属性 attr。
#     def __getattr__(self, attr):
#         # 这里相当于，预先定制一些属性，应对使用者的调用。
#         # 非意料中的属性，则返回一个异常。
#         if attr == 'score':
#             return 99
#         raise AttributeError("'Student' object has no attribute '%s'" %
#                              attr)

# 解释器的运行机制：
# 当解释器调用不存在的属性时，如这里的 score, 那么它会试图调用 __getattr__(self, 'score')
# 来尝试获取属性。

# s = Student()
# s.name() # 'Yud'
# s.score # 99


# 例子二：
# class Chain(object):
#     def __init__(self, path=''):
#         self._path = path
#
#     def __getattr__(self, path):
#         return Chain("%s/%s" % (self._path, path))
#
#     def __str__(self):
#         return self._path
#
# # Chain() 是一个实例，后面一大串是它的属性，
# # 解释器到类中去找“"后面一大串的属性"，没有找到，
# # 于是去执行方法 __getattr__，找是否有预先设定的方法。
# # 该方法中，返回一个实例 chain(path)，这里才看到一个完整的格式--实例化一个类 Chain。
# # 下面这样，不断通过"."连接的调用，不断来到 __getattr__ 中执行。
# # 最后得到结果："/status/user/timeline/list"
# Chain().status.user.timeline.list

# ------------------------------------------------------------------
# 2，使用 __slots__

# python 动态语言的灵活：给实例绑定一个属性
# 如：
# from types import MethodType
#
#
# class Student(object):
#     # 限定该类的实例能够被绑定的属性/方法的名称为：name，或是 age。
#     __slots__ = ('name', 'age')
#
# s = Student()
# # 1, 实例绑定 name 属性
# s.name = 'Yud'
# print(s.name)
#
#
# def set_age(self, age):
#     self.age = age
#
# # 2, 给实例 s 绑定一个方法： set_age
# s.set_age = MethodType(set_age, s)
# s.set_age(25)
# print(s.age)
#
#
# 注意：__slots__ 对于子类是不起作用的。只对当前定义的类的实例起作用。


# ------------------------------------------------------------------
# 3，__str__ 和 __repr__
# str 定义 print(a_instance_of_Aclass) 的内容
# __repr__ 定义 在交互模式中 a_instance_of_Aclas 的返回内容。
