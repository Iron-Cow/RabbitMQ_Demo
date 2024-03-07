import pika
import json

if __name__ == '__main__':
    # Establish connection to RabbitMQ
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(
            host='localhost',
            credentials=pika.PlainCredentials('myuser', 'mypassword')
        )
    )
    channel = connection.channel()

    # Declare the exchange
    # pubsub mode - every consumer notify
    channel.exchange_declare(exchange='orders_exchange', exchange_type='direct')    # Message to be published

    for i in range(100):
        message = {
            'order_id': i,
            'customer_email': 'customer@example.com',
            'items': ['item1', 'item2']
        }
        message_body = json.dumps(message)

        # Publish message
        channel.basic_publish(exchange='orders_exchange',
                              routing_key='order_placed',
                              body=message_body)

        print(F" [x] Sent 'Order {i + 1} Placed' message")

    # Close the connection
    connection.close()
