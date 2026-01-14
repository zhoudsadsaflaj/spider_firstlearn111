import redis
# 连接数据库
r = redis.StrictRedis(host='localhost', port=6379, db=0)
# 创建3 条数据
person1 = {
    'name': '刘硕',
    'age': 34,
    'sex': 'M',
}
person2= {
    'name': '李雷',
    'age': 32,
    'sex': 'M',
}
person3= {
    'name': '韩梅梅',
    'age': 31,
    'sex': 'F',
}
# 将3 条数据以Hash 类型（哈希）保存到Redis中
r.hset('person:1', mapping=person1)
r.hset('person:2', mapping=person2)
r.hset('person:3', mapping=person3)
# 关闭连接
r.connection_pool.disconnect()