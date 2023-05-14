import os
import pika
import aio_pika
import json
from pika.exceptions import ConnectionClosedByBroker, AMQPChannelError, AMQPConnectionError
from services.redis_service import RedisService
from dtos.schedule_dto import ScheduleDto
from services.schedule_db_service import ScheduleDBService
from models.time import Term
import asyncio


r = RedisService()

class Consumer:
    def __init__(self,  queue_name: str):
        self.consume_queue_name = queue_name
        self.host = os.environ.get('RABBITMQ_HOST', 'rabbitmq')
        self.connection = None
        self.channel = None
        self.consume_queue = None
        self.callback_queue = None
        self.response = None
      

    async def consume(self):
        try:
            queue_name = "recommendation"
            username = os.getenv('RABBITMQ_USERNAME')
            password = os.getenv('RABBITMQ_PASSWORD')
            connection = await aio_pika.connect_robust( host=self.host, login=username, password=password)
            async with connection:
                # Creating channel
                channel = await connection.channel()

                # Will take no more than 10 messages in advance
                await channel.set_qos(prefetch_count=10)

                # Declaring queue
                queue = await channel.declare_queue(queue_name, durable= True,
                        exclusive= False,  
                        auto_delete=False,  
                        arguments= None)

                async with queue.iterator() as queue_iter:
                    async for message in queue_iter:
                        async with message.process():
                            json_body = json.loads(message.body)
                            headers = message.headers
                            type = json_body['message']
                            if type == 'create recommendation':
                                await Consumer.process_incoming_message(msg=json_body, headers=headers)


                            if queue.name in message.body.decode():
                                break
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
    async def process_incoming_message(msg, headers):
        try:
            
            """Processing incoming message from RabbitMQ"""
            print('consumed message, processing message')
            
            json_response = msg
            # process the message here
            print(json_response)
            # create recommendation ########
            id = json_response['id']
            type_='recommendation'
            r_key = f"{type_}:{id}"
            r.set_val(key=r_key,val='creating')            
            print(json_response)
            message = json_response['message']
            if message == 'create recommendation':
                # create recommendation ########
                await Consumer.test_create_recommendation(json_response)
                print('recommendation created')
            # recommendation completed, update status
            r.set_val(key=r_key,val='completed')
        except Exception as e:
            print(e)

    @staticmethod
    async def test_create_recommendation(payload):
        try:
            pass
           
        except Exception as e:
            print(e)
            raise e


