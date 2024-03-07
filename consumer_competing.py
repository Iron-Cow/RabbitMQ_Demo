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

    # Ensure the exchange is declared before attempting to bind a queue to it
    channel.exchange_declare(exchange='orders_exchange', exchange_type='direct')

    # Declare the queue
    channel.queue_declare(queue='email_notifications_queue')

    # Bind the queue to the exchange
    channel.queue_bind(exchange='orders_exchange',
                       queue='email_notifications_queue',
                       routing_key='order_placed')

    # Consume messages from the queue
    channel.basic_consume(queue='email_notifications_queue',
                          on_message_callback=callback,
                          auto_ack=True)

    print('Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()