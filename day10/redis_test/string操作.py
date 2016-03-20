#!/usr/bin/env python
# -*- coding:utf-8 -*-

import redis
import time

pool = redis.ConnectionPool(host='127.0.0.1', port=6379)

r = redis.Redis(connection_pool=pool)

r.set("name","felo",ex = 2)
# print r.get("name")
# time.sleep(3)
# print r.get("name")

# r.set("name","alex",nx=True)
# print r.get("name")
#
# r.mset(name = "alex",age=19)
# print r.mget("name","age")

print r.getset("name","alex")
print r.get("name")
print r.getrange("name",1,3)
r.setrange("name",3,"g")
print r.get("name")
print r.bitcount("name")
print r.strlen("name")

r.incr("age",amount=1)
print r.get("age")

r.decr("age",amount=1)
print r.get("age")

r.append("name","exexex")
print r.get("name")

