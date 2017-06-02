# -*- coding: utf-8 -*-

# 定义的 application 函数，“”“”"符合 WSGI 标准（？？？）"的一个 HTTP处理函数。
# environ：包含所有 HTTP 请求信息的 dict 对象。
# start_response：发送 HTTP 响应的函数。

# 函数中调用了 start_response 函数，意味着发送了 HTTP 响应的 Header
# （Header只能发送一次，start_response 函数只能调用一次。？？？）
# 这个函数的两个参数：
# 第一个是 HTTP 响应的字符串，
# 第二个是一个 list 包含了 Header 的信息，
# 它的元素是一个 tuple，tuple 的元素，是两个字符串。

# 我们需要写的是如何响应请求：
# 1，Header 信息，2，返回的内容（这个例子中是一个标签，内容是“"Hello world!"）

# application 的调用由 WSGI 服务器来调用。
# 使用 python 内置的 wsgiref 服务器。


def application(environ, start_response):
    start_response("200 ok", [("Content-Type", "text/html")])
    # PATH_INFO 是地址后面的部分。例如这里的服务器地址写的是：localhost:8000。
    # 而 PATH_INFO ，就是 localhost:8000/web 中的 web。
    body = "<h2>Hello, %s!</h2>" % (environ["PATH_INFO"][1:] or 'web')
    return [body.encode('utf-8')]
