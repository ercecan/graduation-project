import asyncio
import pika

async def consume(channel):
    queue_name = "my_queue"
    await channel.queue_declare(queue=queue_name, durable=True)

    async def callback(ch, method, properties, body):
        # This is the async callback function that will be called
        # when a message is received on the queue
        print("Received message:", body)

    await channel.basic_consume(queue=queue_name, on_message_callback=callback)

    # Start consuming messages
    print("Waiting for messages...")
    while True:
        await asyncio.sleep(1)

async def main():
    connection = await pika.adapters.BlockingConnection()
    channel = await connection.channel()

    await consume(channel)

if __name__ == '__main__':
    asyncio.run(main())