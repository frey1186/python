#!/usr/bin/env python3
#_*_coding:utf-8_*_

import pika
import sys
connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = connection.channel()

channel.exchange_declare(
    exchange="topic_logs",
    exchange_type="topic"
)

route_k = sys.argv[1] or "name"
message =" ".join(sys.argv[2:])  or  "felo"

channel.basic_publish(
    exchange="topic_logs",
    routing_key=route_k,
    body=message
)

channel.close()