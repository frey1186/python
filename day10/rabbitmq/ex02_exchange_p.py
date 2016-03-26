#!/usr/bin/env python3
#_*_coding:utf-8_*_

import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = connection.channel()

#创建一个exchange，类型为fanout，就是所有绑定到这个exchange上的queue都能接受到信息；
channel.exchange_declare(
    exchange="logs",
    exchange_type="fanout"
)

message = " ".join(sys.argv[1:])  or "heloooooooooo......"

#发送消息
channel.basic_publish(
    exchange="logs",  #exchange名称
    routing_key="",   #这里不指定routing_key表示都能接收，这个参数是必须的。
    body=message,

)

channel.close()  #关闭