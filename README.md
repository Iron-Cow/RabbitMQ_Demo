
# RabbitMQ Demo Project

This RabbitMQ demo project demonstrates the implementation of both competing consumers and publish-subscribe (pub-sub) messaging patterns using RabbitMQ with Python. It's structured to showcase how to produce and consume messages in a decoupled architecture, making it a great starting point for understanding RabbitMQ's capabilities in microservices and distributed systems.

## Project Structure

```plaintext
.
├── config
│   └── rabbitmq.conf         # RabbitMQ configuration file
├── consumer_competing.py     # Consumer script for competing consumers pattern
├── consumer_fanout.py        # Consumer script for pub-sub (fanout exchange) pattern
├── docker-compose.yml        # Docker Compose file to run RabbitMQ
├── publisher_competing.py    # Publisher script for competing consumers pattern
├── publisher_fanout.py       # Publisher script for pub-sub (fanout exchange) pattern
├── requirements.txt          # Python dependencies
└── venv                      # Python virtual environment directory
```

## Setup Instructions

1. **Install Dependencies**: Ensure Docker is installed on your system and Python 3.x is available. Create a Python virtual environment and install the Python dependencies listed in `requirements.txt`.

    ```bash
    python -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

2. **Start RabbitMQ Server**: Use Docker Compose to start the RabbitMQ server with the management plugin enabled. The configuration in `docker-compose.yml` and `config/rabbitmq.conf` is used to set up RabbitMQ.

    ```bash
    docker-compose up -d
    ```

3. **Access RabbitMQ Management Console**: Open `http://localhost:15672` in your web browser. The default credentials are set to `user` and `password` as specified in `docker-compose.yml`, unless changed in your setup.

## Running the Demos

### Competing Consumers Pattern

1. **Start the Consumer(s)**: Run one or more instances of `consumer_competing.py` to simulate competing consumers.

    ```bash
    python consumer_competing.py
    ```

2. **Publish Messages**: Run `publisher_competing.py` to publish messages. The messages will be distributed among the active consumers.

    ```bash
    python publisher_competing.py
    ```

### Publish-Subscribe (Pub-Sub) Pattern

1. **Start the Consumer(s)**: Run one or more instances of `consumer_fanout.py` to simulate subscribers in a pub-sub setup.

    ```bash
    python consumer_fanout.py
    ```

2. **Publish Messages**: Run `publisher_fanout.py` to publish messages. Each message will be received by all consumers.

    ```bash
    python publisher_fanout.py
    ```

## Understanding Manual Acknowledgments

In both consumer scripts, manual acknowledgment is implemented to ensure messages are only considered "processed" once the consumer successfully handles them. This ensures reliability and message durability across the system.

## Conclusion

This demo project provides a basic introduction to implementing different messaging patterns with RabbitMQ and Python. It demonstrates the flexibility and power of RabbitMQ in supporting scalable, distributed applications and microservices.

For further exploration, consider implementing additional RabbitMQ features like message durability, priority queues, and delayed messaging.
