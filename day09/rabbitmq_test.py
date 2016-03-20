import pika
conn = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
chan = conn.channel()

