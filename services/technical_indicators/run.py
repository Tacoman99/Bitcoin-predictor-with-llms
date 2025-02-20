from loguru import logger
from quixstreams import Application


def main(
    kafka_broker_address: str,
    kafka_consumer_group: str,
    kafka_input_topic: str,
    kafka_output_topic: str,
    num_candles: int,
):
    """
    3 steps:
    1. Create a Kafka consumer to read the candles from the input topic.
    2. Create a Kafka producer to write the technical indicators to the output topic.
    3. Create a technical indicators calculator.

    Args:
        kafka_broker_address (str): The address of the Kafka broker.
        kafka_consumer_group (str): The consumer group for the Kafka consumer.
        kafka_input_topic (str): The input topic for the Kafka consumer.
        kafka_output_topic (str): The output topic for the Kafka producer.
        num_candles (int): The number of candles to use for the technical indicators.
    """
    print('Hello from technical-indicators!')

    app = Application(
        broker_address=kafka_broker_address,
        consumer_group=kafka_consumer_group,
    )

    input_topic = app.topic(
        name=kafka_input_topic,
        value_deserializer='json',
    )

    output_topic = app.topic(
        name=kafka_output_topic,
        value_serializer='json',
    )

    sdf = app.dataframe(
        topic=input_topic,
    )

    sdf = sdf.update(lambda value: logger.info(f'Candle: {value}'))

    sdf = sdf.to_topic(
        topic=output_topic,
    )

    app.run(sdf)


if __name__ == '__main__':
    from config import config

    main(
        kafka_broker_address=config.KAFKA_BROKER_ADDRESS,
        kafka_consumer_group=config.KAFKA_CONSUMER_GROUP,
        kafka_input_topic=config.KAFKA_INPUT_TOPIC,
        kafka_output_topic=config.KAFKA_OUTPUT_TOPIC,
        num_candles=config.NUM_CANDLES,
    )
