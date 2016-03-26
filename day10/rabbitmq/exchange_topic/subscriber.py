#!/usr/bin/env python3
#_*_coding:utf-8_*_

import pika
import sys
connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = connection.channel()

result = channel.queue_declare(exclusive=True)
q_name = result.method.queue

route_list = sys.argv[1:]

for route_k in route_list:
    channel.queue_bind(
        queue=q_name,
        exchange="topic_logs",    #第一次启动的时候先用subscriber启动不行，需要先有exchange_declare
        routing_key=route_k
    )

def callback(c,m,p,body):
    print("-->",body)

channel.basic_consume(
    consumer_callback=callback,
    queue=q_name
)
channel.start_consuming()