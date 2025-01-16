from pydantic_settings import BaseSettings, SettingsConfigDict

class Config(BaseSettings):
    kafka_broker_address: str
    kafka_topic: str
    model_config = SettingsConfigDict(env_file=".env")

config = Config()
