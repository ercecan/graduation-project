from services.publisher_service import Publisher


publisher = Publisher(queue_name='scheduler')


class ScheduleService():

    def __init__(self):
        pass

    async def create_schedule(self, payload, token='token'):
        try:
            message = payload
            publisher.send_message(message=message, token=token)
            pass
        except Exception as e:
            print(e)
            raise e
        
        
    async def get_schedule(self):
        pass

    async def get_schedules(self):
        pass