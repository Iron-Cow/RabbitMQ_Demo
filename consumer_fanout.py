import pika
import json


def callback(ch, method, properties, body):
    message = json.loads(body)
    print("Received %r" % message)


if __name__ == '__main__':
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(
            'localhost',
            credentials=pika.PlainCredentials('myuser', 'mypassword')
        )
    )
    channel = connection.channel()

    # Declare a fanout exchange
    channel.exchange_declare(exchange='orders_fanout_exchange', exchange_type='fanout')

    # Declare a temporary queue for this consumer
    result = channel.queue_declare('', exclusive=True)
    queue_name = result.method.queue

    # Bind the queue to the exchange
    channel.queue_bind(exchange='orders_fanout_exchange', queue=queue_name)

    channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

    print('Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()