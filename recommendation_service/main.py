from service.consumer_service import Consumer

if __name__ == '__main__':
    consumer = Consumer(queue_name='recommendation')
    consumer.consume()