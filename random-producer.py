from kafka import KafkaProducer
import json
import time
import random
import uuid

# Kafka configuration
bootstrap_servers = 'localhost:9092'
topic_name = 'my_topic'

def generate_random_data():
    """Generate random data for the message"""
    data_types = ['user_event', 'system_metric', 'transaction']
    data_type = random.choice(data_types)
    
    if data_type == 'user_event':
        return {
            "id": str(uuid.uuid4()),
            "type": "user_event",
            "timestamp": time.time(),
            "user_id": random.randint(1000, 9999),
            "event": random.choice(['login', 'logout', 'purchase', 'view']),
            "device": random.choice(['mobile', 'desktop', 'tablet'])
        }
    elif data_type == 'system_metric':
        return {
            "id": str(uuid.uuid4()),
            "type": "system_metric",
            "timestamp": time.time(),
            "server_id": f"srv-{random.randint(1, 20)}",
            "cpu_usage": random.uniform(0.1, 99.9),
            "memory_usage": random.uniform(10.5, 85.2),
            "disk_space": random.uniform(20.3, 95.7)
        }
    else:  # transaction
        return {
            "id": str(uuid.uuid4()),
            "type": "transaction",
            "timestamp": time.time(),
            "transaction_id": f"tx-{random.randint(10000, 99999)}",
            "amount": round(random.uniform(1.0, 1000.0), 2),
            "currency": random.choice(['USD', 'EUR', 'GBP', 'JPY']),
            "status": random.choice(['completed', 'pending', 'failed'])
        }

def produce_messages(count=10, interval=1):
    # Initialize producer
    producer = KafkaProducer(
        bootstrap_servers=bootstrap_servers,
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )
    
    try:
        # Send messages
        for i in range(count):
            # Generate random data
            message = generate_random_data()
            
            # Send to Kafka
            producer.send(topic_name, message)
            print(f"Message {i+1} produced: {message}")
            
            # Wait for specified interval
            time.sleep(interval)
            
        # Ensure all messages are sent
        producer.flush()
        print(f"Successfully produced {count} messages to topic '{topic_name}'")
        
    except Exception as e:
        print(f"Error producing messages: {e}")
    
    finally:
        # Close producer
        producer.close()

if __name__ == "__main__":
    # How many messages to produce
    message_count = 5
    # Seconds between messages
    message_interval = 1
    
    print(f"Starting producer: sending {message_count} messages to '{topic_name}'")
    produce_messages(message_count, message_interval)
