

Kafka Random Data Producer & Consumer




This project implements a Kafka producer and consumer in Python. The producer generates random data and publishes it to a Kafka topic, while the consumer listens to the topic and processes incoming messages.

🚀 Features

    Produces randomly generated data
    Implements Kafka producer & consumer in Python
    Uses Apache Kafka for message streaming


🛠️ Setup
1️⃣ Install Dependencies

Make sure you have Python installed, then install the required library:
````
pip install kafka-python
````
2️⃣ Start Kafka

Kafka needs to be running. If you don’t have it installed, you can use Docker:
````
docker-compose up -d
````

3️⃣ Configure the Producer

You can modify the Kafka settings in producer.py:
```
  bootstrap_servers = 'localhost:9092'  # Kafka broker
  topic_name = 'my_topic'  # Kafka topic name
````
4️⃣ Run the Producer

To start producing messages, run:
````
python random-producer.py
````

🎧 Running the Consumer

The consumer listens for messages and prints them in real-time.

Run the consumer:
````
python consumer.py
````

