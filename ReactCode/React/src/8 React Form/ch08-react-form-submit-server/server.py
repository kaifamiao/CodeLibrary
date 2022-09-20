#!D:\Python\Python37\python
# coding:utf-8

# CGI处理模块
import cgi, cgitb

# 创建 FieldStorage 的实例化
form = cgi.FieldStorage()

# 获取数据
site_username = form.getvalue('username')
site_age = form.getvalue('age')
site_gender = form.getvalue('gender')

import io
import sys
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')

print("Content-type:text/html")
print()
print("<html>")
print("<head>")
print("<meta charset=\"utf-8\">")
print("<title>React to Server</title>")
print("</head>")
print("<body>")
print("<h3>Username:%s</h3>" % (site_username))
print("<h3>Age:%s</h3>" % (site_age))
print("<h3>Gender:%s</h3>" % (site_gender))
print("</body>")
print("</html>")