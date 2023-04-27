import uvicorn
from service.consumer_service import Consumer

if __name__ == '__main__':
    #uvicorn.run('app:app', host="0.0.0.0", port=8003, reload=True)
    consumer = Consumer(queue_name='scheduler')
    consumer.consume()