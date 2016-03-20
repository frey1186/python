import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
channel = connection.channel()

#channel.queue_declare(queue="hello",durable=True)

def call_back(ch, method, properties,body):
    print "-->ch:",ch
    print "-->me:",method
    print "-->pr:",properties
    print "[x] received %r" % body
    import time
    time.sleep(1)
    print 'ok'
    ch.basic_ack(delivery_tag = method.delivery_tag)

channel.basic_consume(call_back,
                      queue="hello",
                      no_ack=True,
                      )

channel.start_consuming()