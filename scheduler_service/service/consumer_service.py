import os
import pika
import json
from pika.exceptions import ConnectionClosedByBroker, AMQPChannelError, AMQPConnectionError
from services.redis_service import RedisService

r = RedisService()

class Consumer:
    def __init__(self,  queue_name: str):
        self.consume_queue_name = queue_name
        self.connection_parameters=pika.ConnectionParameters(host=os.environ.get('RABBITMQ_HOST', 'rabbitmq'))
        print(os.getenv('RABBITMQ_HOST'))
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
                                        on_message_callback=Consumer.process_incoming_message)
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
            self.consume()
        except Exception as e:
            raise e
            
    @staticmethod
    def process_incoming_message(channel, method_frame, header_frame, body):
        try:
            """Processing incoming message from RabbitMQ"""
            print('consumed message, processing message')
            
            json_response = json.loads(body)
            headers = header_frame.headers  # token is headers['token']
            delivery_tag = method_frame.delivery_tag
            channel.basic_ack(delivery_tag)
            # create schedule
            id = json_response['id']
            type_='schedule'
            r_key = f"{type_}:{id}"
            r.set_val(key=r_key,val='creating')            
            print(json_response)

            # create schedule ########

            # schedule completed, update status
            r.set_val(key=r_key,val='completed')
            channel.basic_ack(delivery_tag)
        except Exception as e:
            print(e)
