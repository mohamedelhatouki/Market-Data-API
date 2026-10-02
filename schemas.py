from pydantic import BaseModel
from datetime import date

# الكلاس الأساسي الذي يحتوي على البيانات المشتركة
class MarketSessionBase(BaseModel):
    symbol: str
    session_date: date
    point_of_control: float
    total_volume: float

# كلاس يُستخدم عند إرسال طلب لإضافة بيانات جديدة
class MarketSessionCreate(MarketSessionBase):
    pass

# كلاس يُستخدم عند إرجاع البيانات للمستخدم (يحتوي على المعرف id)
class MarketSession(MarketSessionBase):
    id: int

    # هذا الإعداد ضروري للسماح لـ Pydantic بقراءة البيانات القادمة من SQLAlchemy
    model_config = {"from_attributes": True}