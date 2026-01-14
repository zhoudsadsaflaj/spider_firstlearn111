import MySQLdb

conn=MySQLdb.connect(host='localhost',db='scrapy',user='root',passwd='123456',charset='utf8')
print("--------------sucess")

cur=conn.cursor()

cur.execute('CREATE TABLE person (name VARCHAR(32), age INT, sex char(1)) ENGINE=InnoDB DEFAULT CHARSET=utf8')
print('-----------sucess')

cur.execute('INSERT INTO person VALUES (%s,%s,%s)',('邹雨耀',22,'M'))
print('---------sucess')

conn.commit()
conn.close()