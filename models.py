from sqlalchemy import Column, Integer, String, Float, Date
from database import Base


class MarketSession(Base):
    __tablename__ = "market_sessions"

    id = Column(Integer, primary_key=True, index=True)
    symbol = Column(String, index=True)
    session_date = Column(Date)
    point_of_control = Column(Float)
    total_volume = Column(Float)