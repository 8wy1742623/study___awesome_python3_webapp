# -*- coding: utf-8 -*-

# 1,
# global
# 例如，一个 .py 文件中：
# Money = 2000
#
#
# def add_money():
#     Money += 1
#
# print
# Money
# add_money()

# 第 8 行是会报错的，
# 函数中操作的 Money，是函数局部命名空间中的局部变量。
# 但是，函数中并没有命名该变量。于是会报错。

# 如果需要拿到外面的变量（全局变量），在函数中声明 Money，且加上它是"全局"的声明:
# global Money
# 改正：
# Money = 2000
#
#
# def add_money():
#     global Money
#     Money += 1
#
# print(Money)
# add_money()
# print(Money)


# ------------------------------------------
# 2，with ... as ...
#
