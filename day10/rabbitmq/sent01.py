import pika
import sys
#cred = pika.credentials.PlainCredentials(username="root",password="root")
connection = pika.BlockingConnection(
        pika.ConnectionParameters(host="localhost",port=5672)
        )
channel = connection.channel()

channel.queue_declare(queue="h1")
#默认情况下，重启rabbitmq会使得queue被删除，想要持久化queue，
#需要增加一个durable=True的参数。
#channel.queue_declare(queue="h1",durable=True)

message = " ".join(sys.argv[1:]) or "hello world ..."

channel.basic_publish(exchange="",
                      routing_key="h1",
                      body=message,
                      #重启rabbitmq的时候，消息不能持久化，想要实现持久化
                      #就需要增加下面的参数，注意mode=2
                      properties=pika.BasicProperties(delivery_mode=2)
                      )

print("[x] sending hello world...")
connection.close()