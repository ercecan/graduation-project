import os
import pika
import json
from pika.exceptions import ConnectionClosedByBroker, AMQPChannelError, AMQPConnectionError


class Consumer:
    def __init__(self,  queue_name: str):
        self.consume_queue_name = queue_name
        self.connection_parameters=pika.ConnectionParameters(host=os.environ.get('RABBITMQ_HOST', 'rabbitmq'))
        self.connection = None
        self.channel = None
        self.consume_queue = None
        self.callback_queue = None
        self.response = None
      

    def consume(self):
        try:
            self.connection = pika.BlockingConnection(self.connection_parameters)
            self.channel = self.connection.channel()
            self.channel.basic_qos(prefetch_count=1)
            self.consume_queue = self.channel.queue_declare(queue=self.consume_queue_name)
            self.callback_queue = self.consume_queue.method.queue
            self.channel.basic_consume(queue=self.consume_queue_name,
                                        on_message_callback=self.process_incoming_message)
            try:
                self.channel.start_consuming()
            except KeyboardInterrupt:
                self.channel.stop_consuming()

            self.connection.close()
        except ConnectionClosedByBroker as e:
            print(e)
            raise e
        except (AMQPChannelError, AMQPConnectionError) as e:
            print(e)
            self.connection.close()
            self.run()
        except Exception as e:
            raise e
            

    def process_incoming_message(self, channel, method_frame, header_frame, body):
        try:
            """Processing incoming message from RabbitMQ"""
            print('consumed message, processing message')
            json_response = json.loads(body)
            headers = header_frame.headers  # token is headers['token']
            delivery_tag = method_frame.delivery_tag
            return channel, delivery_tag, headers, json_response
            
        except Exception as e:
            print(e)
