import pika
import time
connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = connection.channel()

channel.queue_declare("h1")

#print("channel-->",channel)
#consumer_callback(channel, method, properties, body)


def callback(ch, method, properties, body):
    #print("ch-->",ch)
    print("reciving message...")
    print("-->",body)
    time.sleep( str(body).count(".") )
    print("Done.")



channel.basic_qos(prefetch_count=1)  #每次接受一条消息，这样保证不同
                                    #的设备能够全负荷使用
channel.basic_consume(callback,"h1",)
channel.start_consuming()