import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
channel = connection.channel()

#channel.queue_declare(queue="hello",durable=True)
channel.basic_publish(exchange="",
                      routing_key="hello",
                      body="hello alex",
                      properties = pika.BasicProperties(delivery_mode=2,),
                      )

print "[x] sending hello world..."
connection.close()