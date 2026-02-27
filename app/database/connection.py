from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("mysql+pymysql://root@localhost/bookstack")

SessionLocal = sessionmaker(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()