import pika
import uuid
import sys
import argparse

class CommandRpcClient(object):
    def __init__(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(
                host='localhost'))
 
        self.channel = self.connection.channel()
 
        result = self.channel.queue_declare(exclusive=True)
        self.callback_queue = result.method.queue
 
        self.channel.basic_consume(self.on_response, 
									no_ack=True,
                                   queue=self.callback_queue)
 
    def on_response(self, ch, method, props, body):
        if self.corr_id == props.correlation_id:
            self.response = body
 
    def call(self, n):
        self.response = None
        self.corr_id = str(uuid.uuid4())
        self.channel.basic_publish(exchange='',
                                   routing_key='rpc_queue',
                                   properties=pika.BasicProperties(
                                         reply_to = self.callback_queue,
                                         correlation_id = self.corr_id,
                                         ),
                                   body=str(n))
        while self.response is None:
            self.connection.process_data_events()
        return self.response

command_rpc = CommandRpcClient()	
#parser = argparse.ArgumentParser()
#parser.add_
#input_cli = parser.parse_args()
input_cli = ''
if len(sys.argv) ==1:
	print("wrong...")
else:
	for i in sys.argv[1:]:
		input_cli += "%s " % i
	print(" [x] Requesting fib(%s)" % input_cli)
	response = command_rpc.call(input_cli)
	if response == "0":
		print(" [.] exce done...")
	else:
		print(" [.] exce failed...")