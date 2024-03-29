import asyncio
import json
import os

import aio_pika
import pika
from dtos.schedule_dto import ScheduleDto
from models.time import Term
from pika.exceptions import (AMQPChannelError, AMQPConnectionError,
                             ConnectionClosedByBroker)
from service.scheduler_service import SchedulerService
from services.redis_service import RedisService
from services.schedule_db_service import ScheduleDBService
from services.school_db_service import SchoolDBService
from utils.schedule_utils import create_preferences, get_ITU_constraints

r = RedisService()

class Consumer:
    def __init__(self,  queue_name: str):
        self.consume_queue_name = queue_name
        self.host = os.environ.get('RABBITMQ_HOST', 'rabbitmq')
        #self.connection_parameters=pika.ConnectionParameters(host=os.environ.get('RABBITMQ_HOST', 'rabbitmq'))
        print(os.getenv('RABBITMQ_HOST'))
        self.connection = None
        self.channel = None
        self.consume_queue = None
        self.callback_queue = None
        self.response = None
      

    async def consume(self):
        try:
            queue_name = "scheduler"
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
                        async with message.process(ignore_processed=True):
                            json_body = json.loads(message.body)
                            await message.ack()
                            headers = message.headers
                            type = json_body['message']
                            if type == 'create schedule':
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
            # create schedule
            type_='schedule'
            student_id = json_response['_id']
            schedule_name = json_response['schedule_name'].strip()
            r_key = f"{type_}:{schedule_name}:{student_id}"
            r.set_val(key=r_key,val='creating')            
            message = json_response['message']
            if message == 'create schedule':
                # create schedule ########
                await Consumer.test_create_schedule(json_response)
            # schedule completed, update status
            r.set_val(key=r_key,val='completed')

        except KeyboardInterrupt:
            print('keyboard interrupt')
            if r_key:
                r.set_val(key=r_key,val='error')

        except Exception as e:
            print(e)

    @staticmethod
    async def test_create_schedule(createScheduleDto):
        try:
            # print("creating schedule")
            major_plan = await SchoolDBService().get_major_plan_by_name(school_name=createScheduleDto['school_name'], major_plan_name=createScheduleDto['major'])
            schedule_service = SchedulerService(get_ITU_constraints(), major_plan)
            create_schedule_dto = createScheduleDto
            term = Term(year=create_schedule_dto['year'], semester=create_schedule_dto['semester'])
            # print("preferences")
            preferences = create_preferences(create_schedule_dto['preferences'])
            
            # print("student")
            student = await schedule_service.create_student_dto(create_schedule_dto["_id"])
            # print("base_schedules")
            base_schedules = await schedule_service.create_base_schedules(student, term, create_schedule_dto["_id"])
            # print("score_schedules")
            scored_schedules = await schedule_service.score_base_schedules(base_schedules, preferences=preferences)
            # print("best_schedules")
            best_schedules = schedule_service.select_best_five_schedules(scored_schedules)
            # print("res")
            response = await schedule_service.create_schedule_objects(student_id=create_schedule_dto['_id'], base_schedules=best_schedules, term=term, preferences=create_schedule_dto["preferences"], schedule_name=create_schedule_dto["schedule_name"])
            #print(response)
            print('finished creating schedule')
        except Exception as e:
            print(e)
            raise e


