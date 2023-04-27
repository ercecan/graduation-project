from services.publisher_service import Publisher


publisher = Publisher(queue_name='recommendation')


class RecommendationService():

    def __init__(self):
        pass

    async def create_recommendation(self, payload, token='token'):
        try:
            message = payload
            publisher.send_message(message=message, token=token)
            pass
        except Exception as e:
            print(e)
            raise e
         
    async def get_recommendation(self):
        pass

    async def get_recommendations(self):
        pass