import redis

r=redis.StrictRedis('localhost',port=6379)
r.set('s','hello world')

print(r.get('s'))

r.rpush('queue',1,2,3)

print(r.llen('queue'))

print(r.lpop('queue'))

print(r.llen('queue'))

print(r.lrange('queue',0,-1))
