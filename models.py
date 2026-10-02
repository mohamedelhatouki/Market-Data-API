from sqlalchemy import Column, Integer, String, Float, Date
from database import Base

class MarketSession(Base):
    # اسم الجدول كما سيظهر في قاعدة البيانات
    __tablename__ = "market_sessions"

    # الأعمدة (Columns)
    id = Column(Integer, primary_key=True, index=True)
    
    # رمز الأصل المالي (مثل EURUSD أو BTC)
    symbol = Column(String, index=True)
    
    # تاريخ الجلسة
    session_date = Column(Date)
    
    # نقطة التحكم (Point of Control) - السعر الذي تم عنده أكبر حجم تداول
    point_of_control = Column(Float)
    
    # إجمالي حجم التداول خلال الجلسة
    total_volume = Column(Float)