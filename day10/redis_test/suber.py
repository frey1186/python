from redis_helper import RedisHelper

obj = RedisHelper()
a = obj.subscribe()


while True:
    msg = a.parse_response()
    print msg
