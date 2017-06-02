---
@ 目录结构：
    backup - 备份目录
    conf - 配置文件
    dist - 打包目录
    docs - 说明文档
    www - Web 目录，存放 .py 文件
        static - 静态文件
        templates - 模板文件
    ios - iOS App 工程
    LICENSE - 代码 LICENSE

---
@ why？

    @ Day2
    1，为什么，Day2，写的 app.py 文件运行之后，是下载文件。而不是显示一个页面。

        解决方法：
            web.Response(body=b'<h1>Awesome</h1>', content_type='text/html')
            在Response函数里添加content_type='text/html'。

    @ Day 3
    （关注细节）
    关键词1：连接池。

        http请求通过“”"连接池"获得数据库连接。