import redis

p = redis.ConnectionPool(host="127.0.0.1")

r = redis.Redis(connection_pool=p)

#print r.get("name")
# r.hset("t1","n","100")
# print r.hget("t1","n")
#
# r.hmset("t1",{"name":"alex",
#              "age":100})
# print r.hmget("t1","name","age")
# print r.hlen("t1")
# print r.hgetall("t1")
