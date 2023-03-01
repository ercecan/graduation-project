import json
import os
import pika


def callback(ch, method, properties, body):
    print("Consumed message by scheduler service")
    '''
    ######
    create schedule and upload to db
    ######
    '''

    json_body = json.loads(body)
    message = json_body['message']
    print(f"consumed message is: {message}")
    new_message = {
        'message': 'start reccomendation',
        'courses': 'schedule'
    }
    try:
        ch.basic_publish(
            exchange='',
            routing_key=os.getenv('RECOMMENDATION_QUEUE'),
            body=json.dumps(new_message),
            properties=pika.BasicProperties(
                delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
            )
        )
    except Exception as e:
        print(e)
        raise e

    ch.basic_ack(delivery_tag=method.delivery_tag)  # acknowledge the message and remove from the queue


def main():
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host="rabbitmq")
    )

    channel = connection.channel()

    channel.basic_consume(
        queue=os.getenv('SCHEDULER_QUEUE'),
        on_message_callback=callback
    )

    print('Waiting for messages on Scheduler queue...')

    channel.start_consuming()


if __name__ == '__main__':
    main()
