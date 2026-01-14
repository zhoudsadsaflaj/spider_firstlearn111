import sqlite3

conn=sqlite3.connect('scrapy.db')
print('-------链接成功----------')
cur=conn.cursor()

cur.execute("CREATE TABLE person(name VARCHAR(32), age INT, sex c)")
print("-------成功创建表格--------")

cur.execute("INSERT INTO person VALUES (?,?,?)",('邹雨耀', 22, 'M'))
print("---------执行成功----------")

conn.commit()
conn.close()