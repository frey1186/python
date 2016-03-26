#!/usr/bin/python3
#_*_coding:utf-8_*_
import pika
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
# channel.queue_declare(queue="test")
channel.basic_publish(exchange='example',
                      routing_key='test',
                      body='Test Message')
connection.close()
