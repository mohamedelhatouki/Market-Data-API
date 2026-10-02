from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# مسار قاعدة البيانات (سيتم إنشاء ملف باسم market_data.db في مجلد المشروع)
SQLALCHEMY_DATABASE_URL = "sqlite:///./market_data.db"

# إذا أردت استخدام MySQL لاحقاً، يمكنك تغيير الرابط ليصبح هكذا:
# SQLALCHEMY_DATABASE_URL = "mysql+pymysql://username:password@localhost/db_name"

# إنشاء المحرك الذي سيتواصل مع قاعدة البيانات
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, 
    # هذا السطر مطلوب فقط لـ SQLite لمنع أخطاء تعدد المسارات (Threads)
    connect_args={"check_same_thread": False} 
)

# إعداد الجلسة (Session) التي سنستخدمها لإضافة أو جلب البيانات
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# إنشاء الكلاس الأساسي الذي سترث منه جميع جداولنا (Models)
Base = declarative_base()