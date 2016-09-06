#!/usr/bin/python
#-*-coding:utf-8-*-
"""
author: chier
content: 初次使用 MySQLdb 类库，简单SQL语句操作
资料： http://www.yiibai.com/python/python_mysql.html
官方网址: http://mysql-python.sourceforge.net/
"""
import MySQLdb

def main():
    conn = MySQLdb.connect (host = "127.0.0.1",port=3356, user = "root", passwd = "secret", db = "anal_db_2016")
    cursor = conn.cursor ()
    cursor.execute ("SELECT VERSION()")
    row = cursor.fetchone ()
    print "MySQL server version:", row[0]


    #创建数据表
    #cur.execute("create table student(id int ,name varchar(20),class varchar(30),age varchar(10))")

    #插入一条数据
    #cur.execute("insert into student values('2','Tom','3 year 2 class','9')")


    #修改查询条件的数据
    #cur.execute("update student set class='3 year 1 class' where name = 'Tom'")

    #删除查询条件的数据
    #cur.execute("delete from student where age='9'")


    cursor.close ()
    conn.close ()

if __name__ == "__main__":
    main()