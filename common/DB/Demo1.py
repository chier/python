# -*- coding: utf-8 -*-
#mysqldb
import sys
import time,MySQLdb
from distutils import log

reload(sys) 
sys.setdefaultencoding('utf8') 


conn=MySQLdb.connect(
		host="localhost",
		port=3356,
		user="root",
		passwd="secret",
		db="test",
		)
cursor = conn.cursor() 

#删除表  
sql = "drop table if exists user"  
cursor.execute(sql)  
  
#创建  
sql = "create table if not exists user(name varchar(128) primary key, created int(10))"  
cursor.execute(sql)  
  
#写入      
sql = "insert into user(name,created) values(%s,%s)"     
param = ("aaa",int(time.time()))      
n = cursor.execute(sql,param)      
print 'insert',n      
     
#写入多行      
sql = "insert into user(name,created) values(%s,%s)"     
param = (("bbb",int(time.time())), ("ccc",33), ("ddd",44) )  
n = cursor.executemany(sql,param)      
print 'insertmany',n      
  
#更新      
sql = "update user set name=%s where name='aaa'"     
param = ("zzz")      
n = cursor.execute(sql,param)      
print 'update',n      
     
#查询      
n = cursor.execute("select * from user")      
for row in cursor.fetchall():      
    print row  
    for r in row:      
        print r      
     
#删除      
sql = "delete from user where name=%s"     
param =("bbb")      
n = cursor.execute(sql,param)      
print 'delete',n      
  
#查询      
n = cursor.execute("select * from user")      
print cursor.fetchall()      
  
cursor.close()      
     
#提交      
conn.commit()  
#关闭      
conn.close()     



# def dbConn():
# 	#连接
# 	log.warn("连接")
# 	ss="连接"
# 	print ss.decode('utf-8')
# 	conn=MySQLdb.connect(
# 		host="localhost",
# 		port=3356,
# 		user="root",
# 		passwd="secret",
# 		db="test",
# 		)
# 	cursor = conn.cursor() 
# 	return "1"

# if __name__ == '__main__':
#     sys.exit(dbConn())
#     # dbConn()



