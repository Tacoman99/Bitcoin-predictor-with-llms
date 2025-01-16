from loguru import logger
from quixstreams import Application
from kraken_api.websocket import KrakenWebsocketAPI

def main(
        kafka_broker_address: str,
        kafka_topic: str,
):    
    """
    It does 2 things:
    1. Reads trades from the Kraken API and
    2. Pushes them to a Kafka topic.

    Args:
        kafka_broker_address: str
        kafka_topic: str
        kraken_api: Union[KrakenWebsocketAPI, KrakenMockAPI]

    Returns:
        None
    """
    
    logger.info("Starting trades service")

    # Initialize the Quix Streams application.
    # This class handles all the low-level details to connect to Kafka.
    app = Application(
        broker_address=kafka_broker_address,
    )

    #Define a topic with json serializer
    topic = app.topic(name=kafka_topic,serializer="json")

    with app.get_producer() as producer:  
        while True:

            for trade in trades:

                # Serialize trades into bytes
                message = topic.serialize(key=trade[pair], value=trade)

                # Push the trade to the topic
                producer.produce(topic, serialized_trade)




if __name__ == "__main__":
    from config import config
    main(config.kafka_broker_address, config.kafka_topic)