import pika
from publisher import Publisher
from consumer import Consumer

import pika

RABBITMQ_HOST = 'localhost'
connection = pika.BlockingConnection(pika.ConnectionParameters(RABBITMQ_HOST))

def main():
    with connection.channel() as channel:
        channel.queue_declare(queue='hello')

        publisher = Publisher(channel)
        publisher.publish('Hello World!', routing_key='hello')

        consumer = Consumer(channel)
        print(' [*] Waiting for messages. To exit press CTRL+C')
        consumer.consume()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)