from kafka import KafkaConsumer
import json
import time

# Kafka configuration
bootstrap_servers = 'localhost:9092'
topic_name = 'my_topic'
consumer_group = 'my-group'

def consume_messages(timeout_sec=30):
    # Initialize consumer
    consumer = KafkaConsumer(
        topic_name,
        bootstrap_servers=bootstrap_servers,
        auto_offset_reset='latest',  # Start consuming from the latest message
        enable_auto_commit=True,
        group_id=consumer_group,
        value_deserializer=lambda x: json.loads(x.decode('utf-8')),
        consumer_timeout_ms=timeout_sec * 1000  # Convert seconds to milliseconds
    )
    
    try:
        print(f"Consumer started. Listening for messages on topic '{topic_name}'...")
        print(f"Will exit after {timeout_sec} seconds of inactivity")
        
        # Track messages received
        message_count = 0
        
        # Consume messages
        for message in consumer:
            message_count += 1
            print(f"\nMessage {message_count} received:")
            print(f"Partition: {message.partition}, Offset: {message.offset}")
            print(f"Timestamp: {time.ctime(message.timestamp/1000)}")
            print(f"Key: {message.key}")
            print(f"Value: {message.value}")
            print("-" * 50)
            
    except KeyboardInterrupt:
        print("\nConsumer stopped by user")
    
    except Exception as e:
        print(f"\nError consuming messages: {e}")
    
    finally:
        # Close consumer
        consumer.close()
        print(f"Consumer closed. Received {message_count} messages in total")

if __name__ == "__main__":
    # How long to wait for new messages before exiting (in seconds)
    timeout = 60
    
    consume_messages(timeout)
