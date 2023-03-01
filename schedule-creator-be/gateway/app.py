import json

import pika
from fastapi import FastAPI
import requests
import os
import dotenv
import json

dotenv.load_dotenv(dotenv.find_dotenv())
app = FastAPI()


def authorize():
    try:
        print('in authorization of gateway')
        response = requests.post(f'http://{os.getenv("AUTH_SVC_ADDRESS")}/login', auth=('erce','123'))
        if response.status_code == 200:
            return True
        return False
    except Exception as e:
        print(e)
        raise e


@app.get('/login')
def login():
    try:
        print('in login of gateway')
        if authorize():
            return True
        return False
    except Exception as e:
        print(e)
        raise e


@app.post('/upload')
def upload():
    try:
        print('in upload of gateway')
        message = {
            'message': 'transcript uploaded, find the remaining classes',
            'transcript_id': 'tr_id',
            'user_id': 'test_user_id'
        }
        connection = pika.BlockingConnection(pika.ConnectionParameters("rabbitmq"))
        channel = connection.channel()
        channel.basic_publish(
            exchange='',
            routing_key='transcript',  # for transcript queue
            body=json.dumps(message),
            properties=pika.BasicProperties(
                delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE  # with this the messages are persisted in the queue
                # in the eventof pod crash or restart
            )
        )
        print('Message sent to transcript queue')
    except Exception as e:
        print(e)
        raise e

