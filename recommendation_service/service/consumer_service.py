import os
import pika
import aio_pika
import json
from pika.exceptions import ConnectionClosedByBroker, AMQPChannelError, AMQPConnectionError
from services.redis_service import RedisService
from .recommendation import RecommendationService
from utils.constraints_util import get_ITU_constraints


r = RedisService()
recommendation_service = RecommendationService(get_ITU_constraints())

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
            connection = await aio_pika.connect_robust( "amqp://guest:guest@127.0.0.1",)
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


                            if 'kill' in message.body.decode():
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
            # create schedule
            type_='recommendation'
            r_key = f"{type_}"
            r.set_val(key=r_key,val='creating')            

            message = json_response['message']
            if message == 'create recommendation':
                student_dto = await recommendation_service.create_student_dto(json_response['student_id'])
                student_dto = await recommendation_service.add_schedule_to_student(student=student_dto, schedule_id=json_response['schedule_id'],
                                                                              semester=json_response['semester'], year=json_response['year'], failed_courses=json_response['failed_courses'])
                future_plan = await recommendation_service.search(schedule_id=json_response['schedule_id'], term_number=json_response['term_number'],
                                                                  student=student_dto, year_=json_response['year'], current_semester_=json_response['semester'])
                print(future_plan)
                #schedule completed, update status
                r.set_val(key=r_key,val='completed')
        except Exception as e:
            print(e)


