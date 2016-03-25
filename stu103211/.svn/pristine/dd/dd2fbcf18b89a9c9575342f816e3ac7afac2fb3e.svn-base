#_*_coding:utf-8_*_
__author__ = 'felo'
import pika
import time
import os

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
 
channel = connection.channel()
 
channel.queue_declare(queue='rpc_queue')
 
def handler(shell_str):
	return os.system(shell_str)

	
 
def on_request(ch, method, props, body):

 
    print(" [.] command: %s" % body)
    response = handler(body)
 
    ch.basic_publish(exchange='',
                     routing_key=props.reply_to,
                     properties=pika.BasicProperties(correlation_id = \
                                                         props.correlation_id),
                     body=str(response))
    ch.basic_ack(delivery_tag = method.delivery_tag)
 
channel.basic_qos(prefetch_count=1)
channel.basic_consume(on_request, queue='rpc_queue')
 
print(" [x] Awaiting RPC requests")
channel.start_consuming()