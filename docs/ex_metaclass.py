#! python3
# -*- coding: utf-8 -*-

# metaclass 练习的复习


# 举例，给自定义的 MyList 增加一个 add 方法。
class ListMetaclass(type):
    # __new__ 方法接受的参数：
    # cls: 将要创建的类的一个实例对象
    # name: 类的名字
    # bases: 类继承的父类的集合
    # attrs: 类的方法的集合
    def __new__(cls, name, bases, attrs):
        # lambda ... 的部分是函数的操作实际过程。
        # 给类添加一个属性/方法：add
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)


# 指定了它的 metaclass 后，创建这个类的时候，需要通过 ListMetaclass.__new__() 来创建。
class MyList(list, metaclass=ListMetaclass):
    pass

l = MyList()
l.add(1)
print(l)