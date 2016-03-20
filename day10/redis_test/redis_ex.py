#_*_coding:utf-8_*_

source = "felo"

for i in source:
    num = ord(i)
    print(bin(num).replace("b",""))


import  redis

r = redis.Redis()
r.set("name","felo")
print(r.get("name"))
r.setbit("name",14,1)
print(r.get("name"))

