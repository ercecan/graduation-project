import json
import uuid
import pika
import os

class Publisher():
    def __init__(self, queue_name: str):
        self.is_running = True
        self.publish_queue_name = queue_name
        self.connection_parameters=pika.ConnectionParameters(host=os.environ.get('RABBITMQ_HOST', 'rabbitmq'))
        self.connection = None
        self.channel = None
        self.publish_queue = None
        self.callback_queue = None
        self.response = None

    def publish(self, message, headers):
        self.connection = pika.BlockingConnection(self.connection_parameters)
        self.channel = self.connection.channel()
        self.publish_queue = self.channel.queue_declare(queue=self.publish_queue_name)
        self.callback_queue = self.publish_queue.method.queue
        self.channel.basic_publish(
            exchange='',
            routing_key=self.publish_queue_name,
            properties=pika.BasicProperties(
                reply_to=self.callback_queue,
                delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE,
                correlation_id=str(uuid.uuid4()),
                headers=headers
            ),
            body=json.dumps(message)
        )
        self.close()

    def send_message(self, message: dict, token: str):
        headers = {
            'token': token
        }
        self.publish(message=message, headers=headers)

    def close(self):
        self.is_running = False
        # Wait until all the data events have been processed
        self.connection.process_data_events(time_limit=1)
        if self.connection.is_open:
            self.connection.close()
