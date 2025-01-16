from datetime import datetime
from pydantic import BaseModel, field_validator
from typing import Optional

class Trade(BaseModel):
    """
    A trade from the Kraken API.
    """
    pair: str
    price: float
    volume: float
    timestamp: datetime
    timestamp_ms: int
    