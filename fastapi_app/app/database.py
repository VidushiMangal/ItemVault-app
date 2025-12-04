#CREATING DATABASE CONNECTION

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.exc import OperationalError

DATABASE_URL = "postgresql://postgres:postgres@localhost/fastapi_db"
engine = create_engine(DATABASE_URL)
try:
    with engine.connect() as conn:
        print(" Database (Postgres) Connected Successfully!")
except OperationalError as e:
    print("Database (Postgres) Connection Failed!")
    print(e)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base=declarative_base()


