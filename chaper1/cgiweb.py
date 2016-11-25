#!/usr/bin/python
# -*- coding:utf-8 -*-

import pymysql

print "Content-Type: text/html\n"
print "<html><head><title>Books</title></head>"
print "<body>"
print "<h1>Books</h1>"
print "<ul>"

connection = pymysql.connect(host='ngaribata.mysql.rds.aliyuncs.com',
                             user='houxr',
                             password='HxrOpDev2016_',
                             db='eh_base_feature4',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
cursor = connection.cursor()
cursor.execute("SELECT userId FROM bus_advice ORDER BY createDate DESC LIMIT 10")

for row in cursor.fetchall():
    print("<li>%s</li>" % row[u'userId'])

print "</ul>"
print "</body></html>"

connection.close()
