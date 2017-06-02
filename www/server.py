# -*- coding: utf-8 -*-

from wsgiref.simple_server import make_server

# todo 1.1 如何才能导入同级目录下的模块
# 这里看起来，程序没有找到该文件。
from docs.study_simple_webapp import application

httpd = make_server("", 8000, application)
print("Serving HTTP on port 8000...")
httpd.serve_forever()
