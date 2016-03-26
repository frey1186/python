#!/usr/bin/python3
#_*_coding:utf-8_*_


import pika

connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = connection.channel()

#产生一个随机名称的queue，并且用完就销毁:exclusive=True
result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue

#将这个queue绑定到exchange=logs上，以接受数据
channel.queue_bind(
    queue=queue_name,
    exchange="logs",
)

#定义callback函数，注意必须四个参数
def callback(c,m,p,body):
    print(body)


#执行basic_consume方法
channel.basic_consume(
    consumer_callback=callback,
    queue=queue_name,

)

#持续接收
channel.start_consuming()