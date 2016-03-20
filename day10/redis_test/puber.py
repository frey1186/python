from redis_helper import RedisHelper

obj = RedisHelper()

while True:
    msg = raw_input(">>")
    obj.public(msg)