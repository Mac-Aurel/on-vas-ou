from app.db.database import engine, Base
from app.models import user, otp

def init_db():
    Base.metadata.create_all(bind=engine)
