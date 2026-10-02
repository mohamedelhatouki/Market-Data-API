from pydantic import BaseModel
from datetime import date


class MarketSessionBase(BaseModel):
    symbol: str
    session_date: date
    point_of_control: float
    total_volume: float


class MarketSessionCreate(MarketSessionBase):
    pass


class MarketSession(MarketSessionBase):
    id: int

    model_config = {"from_attributes": True}